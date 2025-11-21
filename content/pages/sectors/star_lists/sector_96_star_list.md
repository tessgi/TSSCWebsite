Title: Sector 96 Noted TIC Issues
Save_as: sector_96_star_list.html

TIC ID's that had issues in Sector 96.

##Targets not processed in 2-min pipeline and so missing a light curve:
38877693
47552789
80256524
230981971
238196512
255559489

##Targets not processed in 20-sec pipeline and so missing a light curve:
38877693
47552789
80256524
230981971
238196512
255559489

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
214664575
271503437
271503441
280794284
300015238
302134539
350136745
358500970
471013491
506939512

##Targets with aperture warnings in 20-sec data: 
214664575
271503437
271503441
280794284
300015238
302134539
350136745
358500970
471013491


Warnings during
aperture assignment occur when the aperture is discontinuous or clipped, and the resulting
photometry is expected to be unreliable.