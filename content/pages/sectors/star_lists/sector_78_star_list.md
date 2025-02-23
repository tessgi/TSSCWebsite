Title: Sector 78 Noted TIC Issues
Save_as: sector_78_star_list.html


TIC ID's that had issues in Sector 78.

##Targets not processed in 2-min pipeline and so missing a light curve:
51962733, 
255909448, 
329269366, 
518659900, 
2022482049 

For targets that were not processed with the photometric pipeline, the target pixel files
with original and calibrated pixel data are provided, but no light curves are produced. Note
that the target pixel files do not include a background correction for stars without light
curves. The most common reason for a target to not be processed with the photometric
pipeline is that the target exceeds a brightness threshold (Tmag ≲ 1.8) that results in
large pixel stamps. A target located too close to a very bright star, having a comparably
bright companion, impacted by saturated star bleed trails, or having an error in identifying
a clean background region are less common causes for a target to not be processed with
the photometric pipeline. Visual examination of the target along with custom aperture
selection may be needed for photometric analysis of the impacted targets.

##Targets with aperture warnings in 2-min data: 
172751954, 
274221448, 
274221477,
313498719,
354379201,
367912480,
394130313,
441804565,
461523884,
518659900,
1201093741,
2022482049

##Targets with aperture warnings in 20-sec data: 
367912480, 441804565

Warnings during
aperture assignment occur when the aperture is discontinuous or clipped, and the resulting
photometry is expected to be unreliable.