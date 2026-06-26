# Stray light and scatter light study of DMD

##  Stray-Light Characterization

Shaojie paragraph :

Stray light is an important consideration in DMD-based spectroscopic instruments because the DMD itself introduces several potential sources of unwanted scattered light that are not present in conventional fixed-slit spectrographs. Understanding these effects is essential for evaluating the feasibility of DMD technology for astronomical applications.

Several potential sources of stray light were investigated, including diffraction from the periodic micromirror array, scattering from the micromirror surface microstructure, and reflections from the protective window and surrounding package of the DMD chip. A series of laboratory experiments was performed to characterize these effects under different illumination conditions. Despite careful testing, no measurable stray light attributable to the micromirror microstructure or diffraction was identified within the sensitivity of the current experimental setup.

From the perspective of astronomical observations, stray light in the spectroscopic channel is of primary concern, whereas the imaging channel is used primarily for target acquisition and field registration. Therefore, the characterization focused on the spectroscopic optical path. Various DMD mask patterns were applied while long-exposure images were acquired to enhance the visibility of weak scattered-light components.

The experimental results indicate that the dominant sources of stray light are **not the active micromirror array itself**, but rather **reflections from the gold-coated package surrounding the DMD and the protective entrance window**. These effects become more pronounced when ambient light is present during laboratory testing.

To suppress system-level stray light, dedicated optical baffles were incorporated into the instrument, and light-absorbing materials were installed around the DMD package to minimize unwanted reflections. These modifications significantly reduced the observed background level and improved image contrast in the spectroscopic channel.

Based on these investigations, it is also recommended that future DMD-based astronomical instruments employ DMD packages with higher-performance anti-reflection coatings on the entrance window. Reducing the Fresnel reflection from the window surface would further improve stray-light performance and increase overall system throughput.

Small summary :

- dedicated optical baffles were incorporated into the instrument, and light-absorbing materials were installed around the DMD package to minimize unwanted reflections

- higher-performance anti-reflection coatings on the entrance window
- Reducing the Fresnel reflection from the window surface


## Amplitude adaptive optics with a digital micro-mirror device for exoplanet high-contrast imaging, Jan. 2024

Carlotti, A., Baccar, S., Leboulleux, L., Curaba, S., Delboulbé, A., Jocou, L., Moulin, T., Gluck, L., Sztefek, M.-H., n.d. Amplitude adaptive optics with a digital micro-mirror device for exoplanet high-contrast imaging.

In this case, the DMD is used in the optical system pupil plane as an apodizing mask to create high-contrast dark zone around a star to observe exoplanet. The stray light analysis is considered in the way of potentially impacting the exoplanet light interpretation.

In paragraph 4.3 "DMD-induced stray light and ghost", they mention that they "attempt to experimentally measure the amount of stray light by controlling the DMD to send all of the light away from the science path (”all off” state), and measure how much light still reaches the camera". 

They also "do not expect the DMD to be a significant source of stray light, although, given the surface temperature of the device, which is not cooled down, it could be an issue if we were observing in the thermal infrared, or even in the K band", but "have not considered this particular point in our study". 

They do point out that "The DMD may induce a peculiar type of ghost related to the periodic refresh of the array". While the relative intensity of the ghost PSF is "somewhere between ∼ 1.2 10−5 and 5.6 10−5", they conclude that "One could potentially use a shutter synced with the DMD to mask the beam during the refresh", but they "have not attempted to set up this mechanism on the bench, and we may investigate this in the future, although the very short duration of the refresh could make it difficult." Still, they conclude that "It is also not clear whether this ghost PSF would be critical for the observations"

    In conclusion, this DMD in pupil plane could result not in stray light, but as ghost related to the periodic refresh of the array. Still, it is not confirmed whether this ghost PSF would be critical for the observation

## Stray light analysis of SAMOS: a DMD-based multiple object  spectrograph and imager, Aug. 2022

Piotrowski, J.J., Barkhouser, R.H., Smee, S.A., Harding, A.J., Vorobiev, D., Robberto, M., 2022. Stray light analysis of SAMOS: a DMD-based multiple object spectrograph and imager, in: Marshall, H.K., Spyromilio, J., Usuda, T. (Eds.), Ground-Based and Airborne Telescopes IX. Presented at the Ground-based and Airborne Telescopes IX, SPIE, Montréal, Canada, p. 164. https://doi.org/10.1117/12.2630618


 There are multiple article on this DMD-MOS called SAMOS for the SOAR 4.1 meter telescope Cerro Pachón, Chile by Piotrowski et al. :
 
- Piotrowski, J.J., Robberto, M., Smee, S., Barkhouser, R., Donahue, M., Gennaro, M., Harding, A., Hope, S.C., Koeppe, D., Ninkov, Z., Poston, J., Schwartz, L., Tokovinin, A., 2024. On-sky performance of SAMOS: a DMD-based multi-object spectrograph and imager for the SOAR 4.1 meter telescope, in: Vernet, J.R., Bryant, J.J., Motohara, K. (Eds.), Ground-Based and Airborne Instrumentation for Astronomy X. Presented at the Ground-based and Airborne Instrumentation for Astronomy X, SPIE, Yokohama, Japan, p. 28. https://doi.org/10.1117/12.3020796


- Piotrowski, J.J., Vorobiev, D., Robberto, M., Smee, S.A., 2022. Simulation of a digital micromirror device to characterize optical performance in SAMOS: a DMD-based spectrograph, in: Marshall, H.K., Spyromilio, J., Usuda, T. (Eds.), Ground-Based and Airborne Telescopes IX. Presented at the Ground-based and Airborne Telescopes IX, SPIE, Montréal, Canada, p. 165. https://doi.org/10.1117/12.2630651

- Piotrowski, J.J., Smee, S., Hope, S.C., Robberto, M., 2024. In-situ evaluation of DMD contrast ratio using SAMOS: a DMD-based multi-object spectrograph and imager, in: Vernet, J.R., Bryant, J.J., Motohara, K. (Eds.), Ground-Based and Airborne Instrumentation for Astronomy X. Presented at the Ground-based and Airborne Instrumentation for Astronomy X, SPIE, Yokohama, Japan, p. 395. https://doi.org/10.1117/12.3020820


This one focus specifically on the stray light analysis of the optical system. The abstract is pretty interesting.

- Piotrowski, J.J., Barkhouser, R.H., Smee, S.A., Harding, A.J., Vorobiev, D., Robberto, M., 2022. Stray light analysis of SAMOS: a DMD-based multiple object spectrograph and imager, in: Marshall, H.K., Spyromilio, J., Usuda, T. (Eds.), Ground-Based and Airborne Telescopes IX. Presented at the Ground-based and Airborne Telescopes IX, SPIE, Montréal, Canada, p. 164. https://doi.org/10.1117/12.2630618



SAMOS (SOAR Adaptive-Module Optical Spectrograph) is a medium-resolution multi-object spectrograph and imager built to utilize the adaptive optics system of the SOAR telescope in Cerro Pachón, Chile.

Similarly to other DMD usage, they notice that "due to the diffractive and scatter effects of the micromirror array, the inclusion of a DMD requires special considerations when quantifying stray light", with "specular ghost images and scattered light on the SAMOS focal plane arrays". "Our analysis identifies, characterizes, and allows for the mitigation of stray light using a streamlined set of macros written for FRED."

"The motivation for our analysis is to identify any ghost images in the system which arise from specular reflections off of optical and mechanical surfaces"


Their stray light caracterization/analysis method consist of "utilize results from an electromagnetic finite-difference timedomain (FDTD) simulation, along with an opto-mechanical model of SAMOS". "This information is used to recognize problematic opto-mechanical surfaces and make system-level performance predictions. 

"The micromirror array structure of a DMD is similar to a cross-ruled blazed diffraction grating and induces wavelength-dependent diffraction and scatter effects"

They also mention that "This process is applicable to other astronomical instruments and can be used to improve the opto-mechanical design of a wide variety of systems."


"Ray tracing for stray light analysis is conducted in two phases. The first phase is the path search phase. In this phase the sources are traced non-sequentially such that they take any viable optical path to the detector. Ray paths are then recorded and categorized by their interaction type (specular vs. scatter; optical vs. mechanical). Large non-sequential ray traces are computationally expensive, so the search phase is used only to identify stray light paths.  The second phase characterizes the stray light paths found in the search phase. Characterization is done by sequentially tracing each ray path with hundreds of thousands to millions of rays. The sequential traces provide robust models for the total power, peak irradiance, and spatial extent of light on the detector from a ray path.5 For identification and mitigation of stray light, ray paths are organized by the first surface of deviation. Ray paths with a common surface of deviation, such as a reflection off the CCD window, are grouped together. This enables quick identification of surfaces that are leading contributors of stray light."


"This particular ghost image results from a reflection at the window of the DMD. The DMD window is the largest contributor to ghost images in SAMOS because it is near an intermediate focal plane and the window coating is not optimized for the SAMOS bandpass

« It is typical that detector windows are a significant source of ghost images, however, the DMD window anti-reflection coating, which is stock and only optimized for visible wavelengths, is worse than our CCD window coating. » ([Piotrowski et al., 2022, p. 4](zotero://select/library/items/M78J4K8K)) ([pdf](zotero://open-pdf/library/items/IUDRW7CS?page=4&annotation=7C9Z8F8I))



## Design of the spectroscopic ultraviolet multi-object observatory (SUMO) prototype for deployment on the INFUSE sounding rocket, Oct. 2023

Halferty, G., Vorobiev, D., Fleming, B., Chafetz, D., Williams, J., 2023. Design of the spectroscopic ultraviolet multi-object observatory (SUMO) prototype for deployment on the INFUSE sounding rocket, in: Siegmund, O.H., Hoadley, K. (Eds.), UV, X-Ray, and Gamma-Ray Space Instrumentation for Astronomy XXIII. Presented at the UV, X-Ray, and Gamma-Ray Space Instrumentation for Astronomy XXIII, SPIE, San Diego, United States, p. 19. https://doi.org/10.1117/12.2676544


The main important point is just that this is another prototype using custom baffles to "prevent stray light from interfering with other aspects of the instrument", which are "mounted through a thin-plate which can be directly mounted to the base plate".

## Micromirror devices: a new family of MOEMS for the Habitable World Observatory, June 2025

Robberto, M., Gennaro, M., Kassin, S., Smee, S.A., Gong, C., Huffman, J., Ninkov, Z., Puchades, I., 2025. Micro-Mirror-Devices (MMDs): A New Family of MOEMS for the Habitable World Observatory. https://doi.org/10.48550/arXiv.2506.11340


This study mention that "Contrast, i.e., the fraction of background light leaking through the DMD when all elements are tilted to “off” state, has received a lot of attention in the past", but that "an often neglected factor is that contrast is also a strong function of the quality of the device, since faulty open slits leak light that once dispersed contaminates all pixels falling in their spectral trace"

They separate it in two categories : 

- "Scattered light: TI DMD design has a band of “pond” mirrors surrounding the active array of the DMD that are permanently landed in the OFF position. These mirrors represent a potential source of scattered light, as they can reflect light into the spectroscopic or imaging channel especially when the instrument is blasted with light, which is normally the case when taking calibration exposures. These mirrors are masked close to the DMD surface but may receive light if e.g. the calibration optics do not perfectly match the f/# and focal plane of the telescope. Other sources of scattered light include the individual mirror edges and the “via”, the small central structure with thin walls supporting the mirror on top of the torsion hinge.36 Increasing the mirror size is expected to decrease the relevance of these factors."

- "Diffraction: When the size of the mirrors is comparable to the wavelength, diffraction becomes an issue. For astronomical applications, coherence is spatially limited to the size of the PSF; thus, diffraction effects depend mostly on the “slit” used, i.e., the number of illuminated mirrors in the “on” state"s. When a single mirror is used, some diffraction effect may still be caused by the adjacent “off” mirror edges and the underlying structure. In general, the DMD efficiency for a single ON-state micromirror is maximized at short wavelengths and fast focal ratios.34 This drives to larger size the design of DMD mirrors optimized for astronomy."

## Next-generation microshutter arrays for HWO UV multi-object spectroscopy built on the success of the JWST technology, Oct. 2025

Robberto, M., Gennaro, M., Kassin, S., Smee, S.A., Gong, C., Huffman, J., Ninkov, Z., Puchades, I., 2025. Micro-Mirror-Devices (MMDs): A New Family of MOEMS for the Habitable World Observatory. https://doi.org/10.48550/arXiv.2506.11340


Their main point relate to tightly packing individual pixels on the device, such has "there should be no gaps in the shutter structure in the closed position, thus eliminating any path for light leak". Also, "an aluminum light shield is fabricated, which overhangs the gaps" to "stop the light leaking through the gaps between each microshutter blade and the surrounding silicon support structure and torsion hinge".

They also mention that they "aim to reduce light leakage by reducing gaps around the shutter blades through structural, processing, and operation designs"