Title: TESS Data Pipeline (SPOC)
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