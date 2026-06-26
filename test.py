from ximea import xiapi
import cv2
import numpy as np
import os
from datetime import datetime
from astropy.io import fits

# Camera setup configuration
EXPOSURE_START_US = 20000 # exposure intialization (µs)
EXPOSURE_STEP_US = 200 # increment step (µs) w/ +/- keys
MAX_W, MAX_H = 1936, 1216 # for window size
SAVE_DIR = "alignment_captures"
GAIN = 0.0 # en dB

os.makedirs(SAVE_DIR, exist_ok=True)

# Connecting to camera
print('Opening camera...')
cam = xiapi.Camera()
cam.open_device()

cam.set_imgdataformat('XI_MONO16')
exposure = EXPOSURE_START_US
cam.set_exposure(exposure)

img = xiapi.Image()
cam.start_acquisition()

# Window setup
win = 'XIMEA live - laser alignment'
cv2.namedWindow(win, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
use_log = False # initialization pour 

try:
    while True: # to show image continuouly 
        # TODO : Faire en sorte de voir la vue en coupe superposé pour optimiser la finesse
        cam.get_image(img)
        data = img.get_image_data_numpy()  # convert image into numpy array 

        # Find brightest pixel in image (could be change to measure EE in a chosen radius)
        max_val = data.max()
        max_loc = np.unravel_index(np.argmax(data), data.shape)  # (y, x)
        y_max, x_max = max_loc

        # Need to convert 16-bit data into 8-bit (255) to ensure correct display
        if use_log:  # log scale
            log_data = np.log1p(data.astype(np.float32)) # calculate log(x+1) to ensure non zero values in log, in float32 to ensure precision (might not be useful)
            max_log = log_data.max()
            if max_log > 0:
                display = (log_data / max_log * 255).astype(np.uint8)
            else:
                display = np.zeros_like(data, dtype=np.uint8)
        else: # linare scale
            if max_val > 0:
                display = np.clip(data.astype(np.float32) / max_val * 255, 0, 255).astype(np.uint8)
            else:
                display = data.astype(np.uint8)

        # display = np.clip(data.astype(np.float32) / data.max() * 255, 0, 255).astype(np.uint8) if data.max() > 0 else data.astype(np.uint8)
        display_color = cv2.cvtColor(display, cv2.COLOR_GRAY2BGR)

        # marker for
        cv2.drawMarker(display_color, (x_max, y_max), (0, 0, 255),
                        markerType=cv2.MARKER_CROSS, markerSize=20, thickness=1)
        

        h, w = data.shape[:2]
        center_x, center_y = w // 2, h // 2
        offset_x, offset_y = x_max - center_x, y_max - center_y
        profile_x, profile_y = data[y_max, :], data[:, x_max]

        plot_w, plot_h = 250, 100
        if max_val > 0:
            profile_x_rescaled = cv2.resize(profile_x, (plot_w, 1), interpolation=cv2.INTER_AREA).flatten()
            norm_x = (profile_x_rescaled / max_val * (plot_h - 1)).astype(int)
            
            profile_y_rescaled = cv2.resize(profile_y, (plot_w, 1), interpolation=cv2.INTER_AREA).flatten()
            norm_y = (profile_y_rescaled / max_val * (plot_h - 1)).astype(int)

            pts_x = np.array([[i, plot_h - 1 - val] for i, val in enumerate(norm_x)], dtype=np.int32)
            pts_y = np.array([[i, plot_h - 1 - val] for i, val in enumerate(norm_y)], dtype=np.int32)

            margin = 10
            x_offset_top = w - plot_w - margin
            y_offset_top = margin
            
            x_offset_bot = w - plot_w - margin
            y_offset_bot = h - plot_h - margin

            cv2.rectangle(display_color, (x_offset_top, y_offset_top), (x_offset_top + plot_w, y_offset_top + plot_h), (50, 50, 50), -1)
            cv2.rectangle(display_color, (x_offset_bot, y_offset_bot), (x_offset_bot + plot_w, y_offset_bot + plot_h), (50, 50, 50), -1)

            cv2.polylines(display_color, [pts_x + [x_offset_top, y_offset_top]], isClosed=False, color=(255, 100, 0), thickness=2)
            cv2.polylines(display_color, [pts_y + [x_offset_bot, y_offset_bot]], isClosed=False, color=(255, 255, 0), thickness=2)

            cv2.putText(display_color, "Profil X (Horizontal)", (x_offset_top + 5, y_offset_top + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(display_color, "Profil Y (Vertical)", (x_offset_bot + 5, y_offset_bot + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.drawMarker(display_color, (center_x, center_y), (0, 255, 0),
                        markerType=cv2.MARKER_CROSS, markerSize=30, thickness=1)

        mode_text = "LOGARITHMIC" if use_log else "LINEAR"

        info_lines = [
            f"Mode: {mode_text}",
            f"Exposure: {exposure} us",
            f"Max intensity: {max_val} / 65535",
            f"Peak position: ({x_max}, {y_max})",
            f"Offset from center: ({offset_x:+d}, {offset_y:+d}) px",
        ]
        for i, line in enumerate(info_lines):
            cv2.putText(display_color, line, (10, 25 + i * 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1, cv2.LINE_AA)

        # Rescale for display
        scale = min(MAX_W / w, MAX_H / h)
        win_w, win_h = int(w * scale), int(h * scale)
        cv2.resizeWindow(win, win_w, win_h)
        cv2.imshow(win, display_color)

        # User interface : control w/ keyboard key
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('+') or key == ord('='):
            exposure += EXPOSURE_STEP_US
            cam.set_exposure(exposure)
            # print(f"Exposure -> {exposure} us")
        elif key == ord('-'):
            exposure = max(EXPOSURE_STEP_US, exposure - EXPOSURE_STEP_US)
            cam.set_exposure(exposure)
            # print(f"Exposure -> {exposure} us")
        elif key == ord('l') or key == ord('L'):  # Basculer le mode
            use_log = not use_log
            # print(f"Display mode switched to: {'LOG' if use_log else 'LINEAR'}")
        elif key == ord('s'):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            mode_suffix = "log" if use_log else "lin"
            # filename_png = os.path.join(SAVE_DIR, f"capture_DATE{timestamp}_MODE{mode_suffix}_EXP{exposure}.png")
            # cv2.imwrite(filename_png, display_color)
            # filename_fits = os.path.join(SAVE_DIR, f"capture_DATE{timestamp}_MODE{mode_suffix}_EXP{exposure}.fits")
            filename_fits = datetime.now().strftime(f"alignment_captures/capture_{exposure}_%Y%m%d_%H%M%S.fits")
            header = fits.Header()
            header['EXPTIME'] = (exposure, 'Exposure time in milliseconds')
            header['DISPMODE'] = (mode_suffix, 'Display mode (logarithmic or linear)')
            header['DATE-OBS'] = (datetime.now().isoformat(), 'UTC date and time of observation')

            fits.writeto(filename_fits, data, header=header, overwrite=True)
            print(f"Saved: {filename_fits} in {SAVE_DIR}")

finally:
    print('Stopping acquisition...')
    cam.stop_acquisition()
    cam.close_device()
    cv2.destroyAllWindows()
    print('Done.')