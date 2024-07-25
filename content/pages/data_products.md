Title: TESS Data Products Information
template: slide
save_as: data_products.html

<!DOCTYPE html>
<html>


<body>

<p>The four cameras of TESS take consecutive images of a particular region of the sky every 2 seconds. Several data products are produced by the TESS mission from these images: <a href="https://archive.stsci.edu/missions-and-data/tess" target="_blank">Full Frame Images (FFIs), Target Pixel Files (TPFs, also known as postage stamps) of selected targets, and corresponding Light Curves (LCs)</a>. </p>

<p>Each of these is created on-board the spacecraft by co-adding the individual 2-second exposures. These data products are provided in standard FITS format with multiple extensions which contain additional information on calibration, background removal, cosmic-ray rejection, and in the case of the TPFs aperture masks indicating the pixels used to extract the lightcurve. For more information, see the <a href = "https://archive.stsci.edu/missions-and-data/tess/data-products" target = "_blank"> TESS mission page at MAST</a>, the <a href="https://ui.adsabs.harvard.edu/abs/2016SPIE.9913E..3EJ/abstract" target="_blank"> TESS pipeline</a>, as well as the slideshow presented below.</p>

<br></br>

<h2>Types of TESS Data Products</h2>
<br>
TESS identifies targets from a target list onboard the computer, and selects small pixel cut outs around those regions. The FFIs and pixel cut outs are downlinked. The FFIs are then sent to the MAST archive; the pixel cut outs are processed by SPOC into TPFs, and then LCFS. The process is illustrated below. To learn more about these data product, explore the tabs below.</br> 
<img src="https://heasarc.gsfc.nasa.gov/docs/tess/images/tess_ffi_phot.png" class="img-responsive"><figcaption>Pictoral representation of the different TESS data product types. Note that 30-minute FFIs were provided for the primary mission (Cycles 1 and 2). This cadence of FFI images was reduced during subsequent mission extensions. </figcaption></img>
<br></br>


<div class="accordion" id="accordionDataTypes">
  <div class="accordion" id="accordionDataTypes">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingFFI">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFFI" aria-expanded="true" aria-controls="collapseWhy">Full Frame Images (FFIs)</button>
      </h2>
      <div id="collapseFFI" class="accordion-collapse collapse" aria-labelledby="headingFFI" data-bs-parent="#accordionDataTypes" style="">
        <div class="accordion-body">
          <br>
          FFIs are a collection of science and collateral pixels observed simultaneously. A single FFI is the full set of all science and collateral pixels across all CCDs of a given camera. Note that there are 16 CCDs on the spacecraft, each of which is supported by 4 output channels.
          </br>
          <br>
          FFIs are FITS format files containing all pixels on a single CCD. The FFI data is provided in three types: uncalibrated, calibrated, and uncertainty. The uncalibrated FFI data is provided in one file with two Header/Data Units (HDUs): a primary header and the CCD image header and data. The calibrated FFI data and its uncertainty are provided in a separate file with several HDUs: a primary header, the CCD calibrated image header and data, the CCD uncertainty image header and data, and the cosmic ray corrections binary table header and data. TESS FFI images are generally available ~2 weeks after the end of a sector.
          </br>
          <br>
          Note that Cosmic Ray Mitigated FFIs are the same as FFIs except they are collected with the onboard cosmic ray mitigation enabled.
          </br>
          <br>
          The FFIs have observational cadence of 30 minutes (Cycles 1 and 2), 10 minutes (Cycles 3 and 4), and 200 seconds (Cycles 5 and 6).
          </br>
          <br> 
          In addition to the TESS mission pipline-detrended FFIs, TESS Image CAlibrator <a href="https://archive.stsci.edu/hlsp/tica">(TICA)</a> products are <a href="https://archive.stsci.edu/contents/newsletters/february-2023/tica-full-frame-images-now-available-in-tess-cutout-service">now available</a>. These High Level Science Products (HLSPs) were designed as quick-look preview images of TESS FFIs, and are released every half-orbit (~weekly). MAST provides cutouts from the TICA FFIs, as well as the mission FFIs through the <a href="https://mast.stsci.edu/tesscut/">TESSCut</a> service. 
          </br>
          <br>
          To learn more about FFIs and how to use them please see <a href = "https://github.com/spacetelescope/notebooks/blob/master/notebooks/MAST/TESS/beginner_how_to_use_ffi/beginner_how_to_use_ffi.ipynb">this tutorial </a>
          <img class="img-responsive" style="max-width:50%;"src="images/pages/tess_tica.png"><figcaption>Example calibrated full frame image from Sector 27, Camera 1, CCD 1. Image credit: "https://archive.stsci.edu/hlsp/tica</figcaption> </img>
        </div>
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingTPF">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTPF" aria-expanded="true" aria-controls="collapseWhy">Target Pixel Files (TPFs)</button>
    </h2>
    <div id="collapseTPF" class="accordion-collapse collapse" aria-labelledby="headingTPF" data-bs-parent="#accordionDataTypes" style="">
      <div class="accordion-body">
        <br>The Target Pixel Files are the rawest form of target-specific data available at MAST. For each short-cadence target in an observing sector, TESS only acquires the pixels contained within a predefined mask. These pixels are used to create the data found in the light curve files.Each TPF packages these pixels as a time series of images in a binary FITS table. In this binary table, the pixel values are encoded as images. Each element in the binary table contains the pixels from a single cadence. The purpose of these files is to provide the data necessary to perform photometry on the raw or calibrated data when needed (or desired) to understand (or improve) the automated results of the TESS pipeline.
        </br>
        <br>
        If a target is observed in more than one sector, multiple TPFs will be created for that target. Note that they may be made available in separate deliveries to the MAST.
        </br>
        <br>
        The images in the TPF will have dimensions equal to the bounding box of the pixels that were collected for that target. Depending on the location of the target on a CCD, a TPF may therefore contain pixels that do not contain stored data.
        </br>
        <br>
        TPFs will have several HDUs: a primary header, a binary table of images header and data, the aperture mask image header and data, and the cosmic ray correction binary table header and data. The aperture mask image provided with each TPF file indicates the pixels that were collected for the target and which of those pixels were used for photometry.
        </br>
        <br>
        To learn more about TPFs and how to use them please see <a href = "https://github.com/spacetelescope/notebooks/blob/master/notebooks/MAST/TESS/beginner_how_to_use_tp/beginner_how_to_use_tp.ipynb" target = "_blank">this tutorial</a>
        <img class="img-responsive" style="max-width:50%;"src="images/pages/tess_tpf.png"></img>
        </br>
      </div>
    </div>
  </div>
  <div class="accordion" id="accordionDataTypes">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingLC">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseLC" aria-expanded="true" aria-controls="collapseLC">Light Curve Files (LCFs or LCs)</button>
      </h2>
      <div id="collapseLC" class="accordion-collapse collapse" aria-labelledby="headingLC" data-bs-parent="#accordionDataTypes" style="">
        <div class="accordion-body">
          <br>
          Lightcurves are flux time-series produced for each short-cadenced target (from the TPFs) using Simple Aperture Photometry (SAP). LCs are used to search for transiting planets and other astrophysical phenomena. TESS light curves are FITS format files that contain the output of the photometric extraction and subsequent systematics removal (cotrending) performed by the SPOC algorithms. The flux and respective uncertainties are provided at each cadence, with NaNs filling in any missing data values.
          </br>
          <br>
          A single Light Curve File contains the data for one target for on observing sector. Identical to the case for TPFs, if a target was observed in more than one TESS sector, multiple Light Curve Files will be created but they may be made available on the MAST in separate deliveries. Light Curve Files will also consist of several HDUs: a primary header, the light curve photometry binary table header and data, and the aperture mask image header and data. The aperture mask image provided with each light curve is the same as that provided with the corresponding target TPF file.
          </br>
          <br>
          To learn more about LCFs and how to use them please see <a href = "https://github.com/spacetelescope/notebooks/blob/master/notebooks/MAST/TESS/beginner_how_to_use_lc/beginner_how_to_use_lc.ipynb" target = "_blank">this tutorial </a>
          <img class="img-responsive" style="max-width:60%;" src="images/pages/TIC_25375553_S1.png"></img>
        </div>
      </div>
    </div>
  </div>
  <div class="accordion" id="accordionDataTypes">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingHLSP">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseHLSP" aria-expanded="true" aria-controls="collapseHLSP">High Level Science Products (HLSPs)</button>
      </h2>
      <div id="collapseHLSP" class="accordion-collapse collapse" aria-labelledby="headingHLSP" data-bs-parent="#accordionDataTypes" style="">
        <div class="accordion-body">
          High level science products (HLSPs) are community-created products, such as  full-frame image light curves, catalogs, or models. These products are hosted at MAST and openly available to the community. If you are interested in creating a HLSP, we encourage you to <a href = 'https://archive.stsci.edu/contacts.html'> contact MAST</a>. A full list of currently available HLSP for TESS can be found <a href = 'https://archive.stsci.edu/hlsp/'> here</a>, and includes:
          <ul>
            <li><a href='https://archive.stsci.edu/prepds/tess-hermes/'>TESS-HERMES Spectroscopic Survey</a> (PI: Sanjib Sharma)</li>
            <li><a href='https://archive.stsci.edu/prepds/tess-data-alerts/'>Data Products From TESS Data Alerts</a> (PI: Roland Vanderspek)</li>
            <li><a href='http://archive.stsci.edu/hlsp/tasoc'>TESS Data For Asteroseismology Lightcurves</a> (PI: Rasmus Handberg)</li>
            <li><a href='http://archive.stsci.edu/hlsp/cdips'>Cluster Difference Imaging Photometric Survey</a> (PI: Luke Bouma)</li>
            <li><a href='http://archive.stsci.edu/prepds/eleanor'>eleanor FFI Light Curves From TESS</a> (PI: Benjamin Montet)</li>
            <li><a href='http://archive.stsci.edu/hlsp/pathos'>A PSF-Based Approach to TESS High Quality Data Of Stellar Clusters</a> (PI: Domenico Nardiello)</li>
            <li><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS Light Curves From Full Frame Images</a> (PI: Douglas A. Caldwell)</li>
            <li><a href='https://archive.stsci.edu/hlsp/qlp'>TESS Lightcurves From The MIT Quick-Look Pipeline</a> (PI: Chelsea X. Huang)</li>
            <li><a href='https://archive.stsci.edu/hlsp/diamante'>Multi-Sector Light Curves From TESS Full Frame Imaes (DIAMANTE)</a> (PI: Marco Montalto)</li>
            <li><a href='https://archive.stsci.edu/hlsp/stella'>Convolution Neural Networks for Flare Identification in TESS 2-minute Data (STELLA)</a> (PI: Adina Feinstein)</li>
            <li><a href='https://archive.stsci.edu/hlsp/tica'>TESS Image CAlibrator Full Frame Images (TICA)</a> (PI: Michael Fausnaugh)</li>
            <li><a href='https://archive.stsci.edu/hlsp/tess-svc'>The TESS Stellar Variability Catalog (TESS-SVC)</a> (PI: Tara Fetherolf)</li>
            <li><a href='https://archive.stsci.edu/hlsp/tglc'>TESS-Gaia Light Curve ("TGLC")</a> (PI: Timothy D. Brandt)</li>
            <li><a href='https://archive.stsci.edu/hlsp/tess-ebs'>TESS Eclipsing Binaries ("TESS-EBs")</a> (PI: Andrej Prsa)/li>
            <li><a href='https://archive.stsci.edu/hlsp/gsfc-eleanor-lite'>TESS FFI-Based Light Curves from the GSFC Team (GSFC-ELEANOR-LITE)</a> (PI: Brian P. Powell)</li>
            <li><a href='https://archive.stsci.edu/hlsp/smarts'>Simulated TESS Light Curves for Measuring Rotation with Deep Learning ("SMARTS")</a> (PI: Zachary R. Claytor)</li>
            <li><a href='https://archive.stsci.edu/hlsp/tess-coadd-cutouts'>Cutouts from Wide-area TESS Coadded Images ("TESS-COADD-CUTOUTS")</a> (PI: G. Bruce Berriman)</li>
          </ul> 
        </div>
      </div>
    </div>
  </div>    
  <div class="accordion" id="accordionDataTypes">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingCBV">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseCBV" aria-expanded="true" aria-controls="collapseWhy">Cotrending Basis Vectors (CBVs)</button>
      </h2>
      <div id="collapseCBV" class="accordion-collapse collapse" aria-labelledby="headingCBV" data-bs-parent="#accordionDataTypes" style="">
        <div class="accordion-body">
          <br>
          Co-trending basis vectors (CBVs) represent the set of systematic trends present in the ensemble flux data. CBVs are provided for each operational sector of the mission.
          </br>
          <br>
          CBVs are calcualted by the TESS pipeline from a Principle Component Analysis and used to mitigate systematic artifacts within the target light curves. CBVs can be utilized for manual photometric correction more tailored towards the user's science. To learn more about CBVs and how to use them, check out <a href="https://docs.lightkurve.org/tutorials/2-creating-light-curves/2-2-how-to-use-cbvs.html">this tutorial</a>.
          </br>
        </div>
      </div>
    </div>
  </div>
  <div class="accordion" id="accordionDataTypes">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingAux">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAux" aria-expanded="true" aria-controls="collapseWhy">Auxiliary Data Products</button>
      </h2>
      <div id="collapseAux" class="accordion-collapse collapse" aria-labelledby="headingAux" data-bs-parent="#accordionDataTypes" style="">
        <div class="accordion-body">
          <br>
          Additional data products include focal plane characterization files, engineering output, and telemetry data used to calibrate the images and determine the status of the spacecraft. A sample of these data products is displyed below, but for a full list of available products, see the holdings at the <a href="https://archive.stsci.edu/missions-and-data/tess/data-products">MAST</a>.
          </br>
          <u1>
            <li><b>Black level</b>: the mean correction estimated from the virtual black pixel values. There is one metric value per cadence for each CCD readout.
            </li>
            <li><b>2-D black model</b>: the expected readout of a given CCD, in counts, which is observed when no light is incident upon the detector. The model is subtracted from the raw pixel values as part of the calibration process. The model also incorporates the expected black values of collateral pixels. Each CCD has a separate 2-D black model. The size of the model is 2078 x 2136 for each CCD.
            </li>
            <li><b>Smear</b>: correction for shutterless operation. The smear will be less critical for TESS than was needed for Kepler due to the use of frame-transfer in TESS.
            </li>
            <li><b>Gain model</b>: linear approximation to the CCD digitizer performance, in units of photoelectrons per digitizer count. Each TESS CCD has its own gain model containing separate values for each of the 4 readouts on the CCD.
            </li>
            <li><b>Flat field</b>: a model describing the pixel-to-pixel variation in response to photons. This allows the variations in individual pixel response to be removed during calibration. The flat field model is 2048 x 2048 for each CCDs.
            </li>
            <li><b>Linearity</b>: a model describing the deviations from linearity of the CCD digitizers. Each CCD has its own linearity model with separate values for each of the 4 readouts on the CCD. The linearity model is used in conjunction with the gain model of each CCD to convert from a measured number of counts to a flux in photoelectrons.
            </li>
            <li><b>Read noise</b>: an estimate of the variation in pixel values caused by the digitization process itself. This is separate from the noise due to Poisson variation in the number of photons collected from a target (``shot noise''). The read noise model is used in the calibration process to estimate the uncertainty in pixel values, which is incorporated into the uncertainty propagation process. Each CCD has its own read noise model with separate values for each of the 4 readouts on the CCD.
            </li>
            <li><b>Dark current</b>: the mean dark current calculated from the virtual row pixel values. There is one metric value per cadence for each readout. 
            </li>
          </u1>
        </div>
      </div>
    </div>
  </div>
  <div class="accordion" id="accordionDataTypes">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingCollateral">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseCollateral" aria-expanded="true" aria-controls="collapseWhy">Collateral (Non-science) Pixels</button>
      </h2>
      <div id="collapseCollateral" class="accordion-collapse collapse" aria-labelledby="headingCollateral" data-bs-parent="#accordionDataTypes" style="">
        <div class="accordion-body">
          <br>
          Collateral data includes pixels from leading and trailing virtual columns, leading and trailing masked rows, and trailing virtual rows (in units of ADC counts).
          </br>
          <br>
          Additional collateral data includes auxiliary instrument models which describe the calibration effects.
          </br>
          <br>
          Pixel calibration is performed on both the cadence pixels and Full Frame Image (FFI) pixels, and calibrated science pixel values, in photoelectrons, along with their uncertainties are archived at the MAST.            
          </br>
          <img class="img-responsive" style="max-width:50%;" src="images/pages/tess_collateralPix.png">
        </div>
      </div>
    </div>
  </div>    
  <div class="accordion" id="accordionDataTypes">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingSim">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseSim" aria-expanded="true" aria-controls="collapseSim">Simulated Data</button>
      </h2>
      <div id="collapseSim" class="accordion-collapse collapse" aria-labelledby="headingSim" data-bs-parent="#accordionDataTypes" style="">
        <div class="accordion-body">
          <br>
          During the development of a space mission, several End-to-End tests are conducted, which include testing the pipeline and the data transfer between different institutions. To do this various data products are simulated, these data can be very useful to the community, and aid potential TESS users in the development of tools and in assessing the feasibility of an investigation.
          </br>
          <br>
          Data for the "End-To-End 6" can be found <a href = "https://archive.stsci.edu/missions-and-data/tess/data-products/ete-6" target = "_blank">here.</a>              
          </br>
        </div>
      </div>
    </div>
  </div>
</div>




<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>

</body>
</html>