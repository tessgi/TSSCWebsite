Title: TESS Data Pipeline and Data Access Information
template: slide
save_as: data_pipeline.html

The flow of data from the spacecraft to its final archive involves participation from multiple institutions that make up the TESS project team. The TESS data processing pipeline itself was developed by the Science Processing Operations Center (SPOC) at NASA Ames Research Center and builds on the legacy of the Kepler data processing pipeline. A brief overview of how TESS data is handled and the pipeline is presented below, with more details available in the documentation page REF.

<h1> Pipeline overview </h1>

<br/>
<img class="img-responsive" style="max-width:75%;" src="https://heasarc.gsfc.nasa.gov/docs/tess/images/mission/tess_operations2.png">
<br/>

Data from the TESS spacecraft are downloaded through the Deep Space Network (DSN) and delivered to the Payload Operations Center (POC) at the <a href = 'https://tess.mit.edu'>Massachusetts Institute of Technology (MIT)</a>. The POC sends uncalibrated requantized pixel data, target lists, spacecraft configuration and engineering data, and focal plane characterization models (for calibration) to the Science Processing Operations Center (SPOC) at <a href = 'https://www.nasa.gov/ames/tess-pipeline'>NASA AMES</a>

The SPOC calibrates the science data in two steps, first by the orbit and then by the sector. The SPOC uses instrument calibration models provided by the POC to calibrate all science data. Once a full sector is calibrated the transiting planet search software is run by the SPOC to identify and flag threshold crossing events (TCEs). Calibrated target pixels and FFIs, light curves generated from 20-sec and 2-min cadence targets, and TCEs are sent to the TESS Science Office (TSO, which includes MIT and the Smithsonian Astrophysical Observatory, SAO).

The TSO is responsible for detailed analysis of TCEs and the identification of TESS Objects of Interest (TOIs). The TSO delivers the lists of TOIs to the <a href = 'https://archive.stsci.edu/tess/'>Mikulski Archive for Space Telescopes (MAST), located at the Space Telescope Science Institute (STScI) </a> along with dispositions and information documenting the vetting process for each TOI on a regular schedule, nominally every four months.

<h1> Data Access </h1>

The processed data and meta-data from the SPOC are archived at <a href = 'https://archive.stsci.edu/tess/'>(MAST)</a>, which is the official (and primary) science data archive for TESS. You can find more informatio on data access, tools, and resources at the <a href = 'http://archive.stsci.edu/tess/summary.html'> MAST TESS Summary Page</a>. Brief descriptions on the various data products avaliable at the <a href = 'https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html'>MAST Portal </a> are provided below. 

<h1> TESS Input Catalog (TIC) </h1>

To meet the goals of the primary mission, an all-sky catalog was generated to act as a basis for target selection. The TESS Target Selection Working Group (TSWG) was tasked with the creation and maintenance of the catalog with the aim of compiling every optically luminous, persistent object in the sky down to the limits of available wide-field photometric catalogs including both point sources and extended sources. This enables the selection of optimal targets to search for small transiting planets and allows flux contamination to be calculated in an optimal aperture for each target (critical due to the 21 arcsec TESS pixels). The resulting <a href = 'https://arxiv.org/pdf/1905.10694.pdf'> "The Revised Tess Input Catalog And Candidate Target List" </a> is the source from which the >200,000 primary mission targets were selected and is known as the TESS Input Catalog (TIC).

The TIC was assembled based on the Gaia DR2 catalog, and augmented with data from many additional catalogs to create a full list of point sources and extended sources that could be observed by TESS. The input catalog data are used to determine the physical and observational parameters of many of the TIC stars, including stellar radius, stellar mass, and effective temperature. TIC-8 includes 1.7 billion point sources and about 100 million extended sources. A visual overview of the input catalogs and methodology used to construct the TIC is shown in the schematic below.

<br/>
<img class="img-responsive" style="max-width:90%;" src="https://heasarc.gsfc.nasa.gov/docs/tess/images/giprogram/tic8_overview_figure2.png"><figcaption>Overview of the photometric catalogs used to construct the TESS Input Catalog (TIC). Yellow arrows depict the order that catalogs are cross-matched and/or merged. The final TIC (TIC-8 as of 2019-06-01) is represented by the green box at the upper right. Image Credit: [Stassun et al. 2019](https://ui.adsabs.harvard.edu/abs/2019arXiv190510694S/abstract).</figcaption>
<br/>

The TIC can be directly accessed through the <a href = 'https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html'>MAST Portal </a> by first selecting MAST Catalogs as the collection and then TESS Input v8 as the Mission. A full description of the assembly, content, and properties of the TIC can be found in the <a href = 'https://arxiv.org/pdf/1905.10694.pdf'> Stassun et al. (2019) </a> paper. 

<h1> The Candidate Target List (CTL) </h1>
The Candidate Target List (CTL) is a subset of the TIC. This is a set of targets selected as likely good targets for transit detection and consists of two main components.

  - All TIC stars brighter than TESS magnitude = 13, and an estimated stellar radii smaller than RSun.
  - All stars included in the <a href = 'https://arxiv.org/abs/1710.00193'> curated Cool Dwarf Catalog (CDC) </a>.

The CTL is a list of about 9.5 million stars, each evaluated according to a metric that prioritizes the star for transit detection, which incorporate the TESS magnitude, stellar radius, estimated flux contamination, and number of sectors of observation. You can search the CTL datatabe please at the MAST Portal by selecting MAST Catalogs as the collection and then TESS CTL v8.01 as the Mission. For more information on the TIC and CTL please visit the <a href = 'https://tess.mit.edu/science/tess-input-catalogue/'> MIT page </a>.

<h1> <a href = 'https://astroquery.readthedocs.io/en/latest/mast/mast.html'> MAST API/astroquery </a> </h1>

This allows the user to search for, and retrieve, TESS data products programmatically based on a list of coordinates or target names, interact with observational data, TIC, and CTL catalogs in custom programs.

<h1> <a href = 'https://exo.mast.stsci.edu/'> exo.MAST </a> </h1> 

Here you can find MAST data (including TESS) for known planets and TOIs, matched to orbital phase.
You can also plot sector-stitched Data Validation light curves, as well as access exoplanet parameters with references.

<h1> <a href = 'https://exofop.ipac.caltech.edu/tess/index.php'> ExoFOP-TESS </a> </h1> 

ExoFOP-TESS optimizes resources and facilitates collaboration in follow-up studies of targets observed by TESS. The portal provides stellar parameters from the TESS Input Catalog (TIC), which is served by the MAST archive, and planet parameters from the <a href = 'https://exoplanetarchive.ipac.caltech.edu'> NASA Exoplanet Archive </a>. 

<h1> <a href = 'https://mast.stsci.edu/tesscut/'> TESSCut </a> </h1> 
TESSCut allows the user to create custom time series pixel cutouts from the TESS full frame images and find out what sectors / cameras / detectors a target was observed in. Further information about TESSCut can be found <a href = 'https://astroquery.readthedocs.io/en/latest/mast/mast.html#tesscut'> here </a>

<h1> <a href = 'http://archive.stsci.edu/tess/bulk_downloads.html'> Bulk downloads </a> </h1> 
Here, you can:

* Download all light curves / target pixel files for a given sector.
* Download all light curves / target pixel files for a given GI program.
* Download all full frame images for a given sector.
* Download the entire TOI or TCE table.
* Download the current TIC and CTL.

<h1> <a href = 'https://outerspace.stsci.edu/display/TESS/TESS+Archive+Manual'> Archive manual </a> </h1> 
The manual provides step-by-step instructions on how to:

* use MAST web interfaces for TESS
* obtain Python notebook tutorials on using TESS data and MAST tools
* access the TIC and CTL "live" release notes
* learn how to contribute TESS-related data products to MAST

<h1> Data products at MAST </h1> 
The following TESS data products and catalogs are currently available at MAST:

* Two-minute cadence target pixel files
* Two-minute cadence light curves
* Twenty-second cadence target pixel files
* Twenty-second cadence light curves
* Data validation time series files
* Full frame images (calibrated and uncertainty files)
* Cotrending basis vectors files
* Simulated Data files
* Artifact removal pixel files
* Background pixel files
* Auxiliary data for calibration
* Collateral data files
* Reverse clock files
* Ancillary engineering files
* Latest SPICE kernels (bsp and tsc binary files)

**Catalogs at MAST**

* TESS Input Catalog (TIC)
* Candidate Target List (CTL)
* Revised stellar parameters of Kepler targets (Q1-Q16)
* Revised stellar parameters of Kepler targets (Q1-Q17)
* Kepler Objects of Interest (KOI)
* Kepler/GALEX cross match catalog
* False positive working group tables
* Observed targets by quarter

For more information about the specific products that TESS provides see our Data Product Information Page (data-products.html).