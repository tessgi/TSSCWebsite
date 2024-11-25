Title: TESS Data Analysis Tools
template: slide
save_as: data-analysis-tools.html


<p>Here you can find information on the various community products, software tools, and efforts developed specifically for TESS data, or can be used or modified for TESS data. Note that tools and utilities are continuously under development by the community, and some can be more robust than others. The TESS Science Support Center periodically updates this list as new tools, software, and tutorials become available. </p>

<p>If you have any tools you would like us to include or highlight, please contact us at <a href="https://heasarc.gsfc.nasa.gov/docs/tess/helpdesk.html" target="_blank"> TESS GI Helpdesk</a> or tesshelp@bigbang.gsfc.nasa.gov</p>

### Lightkurve
<p><a href = 'https://lightkurve.github.io/lightkurve/'>Lightkurve</a> is a Python-based package developed by the Kepler/K2 Guest Observer (GO) Office for use by the community to work with Kepler and K2 data. The TESS GI Office has partnered with the Kepler/K2 GO Office to adapt Lightkurve for use with TESS data. </p>
<p>Lightkurve functionality includes:
  <li>Searching for, reading, and interacting with the MAST holdings for available FFI, TPF, and LC mission products and high level science products </li>
  <li>Extracting light curves from pixels using custom aperture photometry or custom PSF fitting</li>
  <li>Removing trends or correcting systematics using widely-used, standard methods (SavGol, CBVs, SFF, ...)</li>
  <li>Identifying periodic signals, such as transits or stellar rotation through periodograms</li>
</p>
You can access the code, report issues, or submit pull requests at the <a href = 'https://github.com/lightkurve/lightkurve'>lightkurve git repository</a>.



### Community Software Packages
In addition to the mission-supported pipeline and lightkurve package, a number of open-source tools have been created by community members that can be helpful for analyzing and interpreting TESS data. We include a non-exhaustive list of packages in the following dropdowns. 
<div class="accordion" id="accordionCommunityTools">
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingDetrending">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseDetrending" aria-expanded="true" aria-controls="collapseDetrending">Detrending and Analysis</button>
    </h2>
    <div id="collapseDetrending" class="accordion-collapse collapse" aria-labelledby="headingDetrending" data-bs-parent="#accordionCommunityTools" style="">
      <div class="accordion-body">
        <table class="table table-striped table-hover" style="max-width:55em;">
        <tr>
          <td style="width: 15em;"><a
          href='https://github.com/waqasbhatti/astrobase'>astrobase</a></td>
          <td> Light curve tools and analysis <a href='https://github.com/waqasbhatti/astrobase-notebooks'>A tutorial can be found here</a>.
          </td>
        </tr>
        <tr>
          <td style="width: 15em;"><a
          href='https://github.com/hvidy/halophot/'>halophot</a></td>
          <td> K2 Halo Photometry for very bright stars. Can be applied to TESS data.</td>
        </tr>
        <tr>
          <td style="width: 15em;"><a
          href='https://github.com/saigrain/k2scTess'>k2scTess</a></td>
          <td>TESS systematics correction via simultaneous modeling of stellar variability and jitter-dependent systematics using Gaussian Process regression.</td>
        </tr>
        <tr>
          <td style="width: 15em;"><a
          href='https://github.com/lightkurve/lightkurve/tree/main'> Lightkurve</a></td>
          <td> A user-friendly package for supporting science and performing lightcurve analysis with data from Kepler, K2, and TESS. <a href='https://github.com/lightkurve/lightkurve/tree/main/docs/source/tutorials'> Tutorials can be found here</a>.
          </td>
        </tr>
        <tr>
          <td style="width: 15em;"><a
          href='https://github.com/stephtdouglas/PySysRem'>PySysRem</a></td>
          <td>Correct systematic effects in large sets of photometric light curves.</td>
        </tr>
        <tr>
          <td style="width: 15em;"><a
          href='https://github.com/nksaunders/skope'>skope</a></td>
          <td>scope creates a forward model of telescope detectors with pixel sensitivity variation, and synthetic stellar targets with motion relative to the CCD. It allows for the creation of light curves and as simulations of Kepler/K2/TESS data.</td>
        </tr>
        <tr>
          <td style="width: 15em;"><a
          href='https://wotan.readthedocs.io/en/latest/Installation.html'>wotan</a></td>
          <td>Offers free and open source algorithms to automagically remove trends from time-series data. Tutorials can be found <a href='https://github.com/hippke/wotan/tree/master/tutorials'>here.</a>
          </td>
        </tr>
        </table>
      </div>
    </div>
  </div>
  <div class="accordion" id="accordionCommunityTools">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingFFIanalysis">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFFIanalysis" aria-expanded="true" aria-controls="collapseFFIanalysis">Full Frame Image (FFI) Handling</button>
      </h2>
      <div id="collapseFFIanalysis" class="accordion-collapse collapse" aria-labelledby="headingFFIanalysis" data-bs-parent="#accordionCommunityTools" style="">
        <div class="accordion-body">
          <table class="table table-striped table-hover" style="max-width:55em;">
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/ryanoelkers/DIA'>DIA</a></td>
            <td>Difference Imaging Analysis to extract a light curve from FFIs.</td>
          </tr>
          <tr>
            <td style="width: 15em;"><a href='http://adina.feinste.in/eleanor/index.html'>eleanor</a></td>
            <td>eleanor is an open-source python framework for downloading, analyzing, and visualizing data from the TESS Full Frame Images.</td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://filtergraph.com/tess_ffi/'>Filtergraph</a></td>
            <td>This is the TESS full-frame-image (FFI) portal which hosts the
            data products from the pipeline of <a href='http://adsabs.harvard.edu/abs/2018AJ....156..132O'>Oelkers & Stassun (2018).</a>
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a href='http://www2.iap.fr/users/alard/package.html'>ISIS</a></td>
            <td>Process CCD images using image subtraction.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://docs.lightkurve.org'>Lightkurve</a></td>
            <td> Extract light curves from FFIs, and package into TPFs.
            </td>
          </tr>
        <tr>
            <td style="width: 15em;"><a
            href='https://github.com/zkbt/spyffi'>SpyFFI</a></td>
            <td>Tools for simulating TESS imaging at multiple cadences, including light curves, jitter, focus drifts, cosmic rays.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://mast.stsci.edu/tesscut/ '>TESSCut</a></td>
            <td> Create time series pixel cutouts from the TESS FFIs. Find out what sectors/cameras/detectors a target was observed in.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/keatonb/TESS_PRF'>TESS_PRF</a></td>
            <td>Tools to display the TESS pixel response function (PRF) at any location on the detector.
            </td>
          </tr>
            <tr>
            <td style="width: 15em;"><a
            href='https://github.com/lightkurve/lkprf/tree/main'>lkprf</a></td>
            <td>Tools to work with the TESS pixel response function (PRF) files for Kepler and TESS.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/CheerfulUser/TESSreduce'>TESSreduce</a></td>
            <td>This builds on lightkurve, allowing the user to reduce TESS data while preserving transient signals. The user can supply a TPF or give coordinates and sector to construct a TPF with TESScut. The background subtraction accounts for the smooth background and detector straps. Alongside background subtraction TESSreduce also aligns images, performs difference imaging, and can even detect transient events!
            </td>
          </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
  <div class="accordion" id="accordionCommunityTools">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingPosition">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapsePosition" aria-expanded="true" aria-controls="collapsePosition">Data Access and Positional Tools</button>
      </h2>
      <div id="collapsePosition" class="accordion-collapse collapse" aria-labelledby="headingPosition" data-bs-parent="#accordionCommunityTools" style="">
        <div class="accordion-body">
          <table class="table table-striped table-hover" style="max-width:55em;">
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/lightkurve/lksearch'>lksearch</a></td>
            <td> Allows users to search for and download mission products from TESS, Kepler, and K2, including access to cloud-based products. Also enables cross-catalog searches. 
            </td>
          </tr>
          <tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://pypi.org/project/tesswcs/'>tesswcs</a></td>
            <td> Will enable you to create an astropy World Coordinate System for any pointing of the TESS telescope. You can access both the true WCS from archival data, and predict the WCS for a given RA, Dec, and spacecraft roll.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/christopherburke/tess-point'>tess-point</a></td>
            <td> Provides the target ecliptic coordinates, TESS sector number, camera number, detector number, and pixel column and row.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py/'>TESS-point Web Tool</a></td>
            <td>A tool which uses tess-point for determining whether stars and galaxies are observable by TESS, and in which sector.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/tessgi/toco'>toco</a></td>
            <td>A way to quickly see some info about a star based on it's TICID.
            </td>
          </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
  <div class="accordion" id="accordionCommunityTools">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingPlanetFit">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapsePlanetFit" aria-expanded="true" aria-controls="collapsePlanetFit">Planet search, modeling, and vetting</button>
      </h2>
      <div id="collapsePlanetFit" class="accordion-collapse collapse" aria-labelledby="headingFFIanalysis" data-bs-parent="#accordionCommunityTools" style="">
        <div class="accordion-body">
          <table class="table table-striped table-hover" style="max-width:55em;">
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/lkreidberg/batman'>batman</a></td>
            <td>Fast transit light curve models in Python.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://exogram.vercel.app'>Exogram</a></td>
            <td>Online toolkit for vetting and validation of TESS data. </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/exoplanet-dev/exoplanet'>exoplanet</a></td>
            <td> Toolkit for probabilistic modeling of time series data in astronomy with a focus on observations of exoplanets
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/3fon3fonov/exostriker'>ExoStriker</a></td>
            <td>Performs N-body simulations, and models the RV stellar reflex motion caused by dynamically interacting planets in multi-planetary systems.
            </td>
          </tr>
           <tr>
            <td style="width: 15em;"><a
            href='https://juliet.readthedocs.io/en/latest/index.html'>Juliet</a></td>
            <td>A versatile modelling tool for transiting and non-transiting exoplanetary systems that allows users to perform quick-and-easy fits to data coming from transit photometry, radial velocity or both using bayesian inference and, in particular, using Nested Sampling in order to allow both efficient fitting and proper model comparison. Tutorials can be found <a href='https://juliet.readthedocs.io/en/latest/tutorials/transitfits.html'>here.</a>
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/hpparvi/k2ps'>k2ps</a></td>
            <td>K2 planet search.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/mrtommyb/ktransit'>ktransit</a></td>
            <td>A simple exoplanet transit modeling tool in Python.
            </td>
          </tr>
        <tr>
            <td style="width: 15em;"><a
            href='https://github.com/matiscke/lcps'>lcps</a></td>
            <td>A tool for pre-selecting light curves with possible transit signatures.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/rodluger/planetplanet'>planetplanet</a></td>
            <td>A general photodynamical code for exoplanet light curves.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/rodluger/pysyzygy'>pysyzygy</a></td>
            <td>A fast and general planet transit (syzygy) code written in C and in Python.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/hpparvi/PyTransit'>PyTransit</a></td>
            <td>Fast and easy transit light curve modeling using Python and Fortran.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/petigura/terra'>terra</a></td>
            <td>Transit detection code.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/mindriot101/ttvfast-python'>ttvfast-python</a></td>
            <td>Python interface to the TTVFast library.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/exoplanetvetting/DAVE'>DAVE</a></td>
            <td> Find and vetting planets using data from K2 and TESS.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/timothydmorton/VESPA'>VESPA</a></td>
            <td>Calculating false positive probabilities for transit signals.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/stevengiacalone/triceratops'>Triceratops</a></td>
            <td> Vetting and validating TESS Objects of Interest.
            </td>
          </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
  <div class="accordion" id="accordionCommunityTools">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingMisc">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseMisc" aria-expanded="true" aria-controls="collapseMisc">Miscellaneous science tools</button>
      </h2>
      <div id="collapseMisc" class="accordion-collapse collapse" aria-labelledby="headingMisc" data-bs-parent="#accordionCommunityTools" style="">
        <div class="accordion-body">
          <table class="table table-striped table-hover" style="max-width:55em;">
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/stephtdouglas/animate_spots'>animate_spots</a></td>
            <td>Make frames for animated gifs/movies showing a rotating spotted star.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/ekaterinailin/AltaiPony'>AltaiPony</a></td>
            <td>Python-based flare finding code for Kepler/K2/TESS light curves.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://emac.gsfc.nasa.gov/'>EMAC</a></td>
            <td>The NASA Goddard Space Flight Center Exoplanet Modeling and
            Analysis Center (EMAC) serves as a repository and integration platform for modeling and analysis resources focused on the study of exoplanet characteristics and environments.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://fast-lightcurve-inspector.osc-fr1.scalingo.io'>FLI</a></td>
            <td>Online toolkit for visual inspection of TESS data. </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/skgrunblatt/FoFreeAST'>FoFreeAST</a></td>
            <td>Fourier-Free Asteroseismology: uses celerite to model granulation and oscillations of stars.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/timothydmorton/isochrones'>isochrones</a></td>
            <td>Pythonic stellar model grid access; easy MCMC fitting of stellar properties.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/danxhuber/isoclassify'>isoclassify</a></td>
            <td>Perform stellar classifications using isochrone grids.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/barentsen/k2flix'>k2flix</a></td>
            <td>Create quicklook movies from the pixel data observed by Kepler/K2/TESS.
            </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='http://latte-online.flatironinstitute.org/app'>LATTE</a></td>
            <td>Online toolkit for visual inspection of TESS data. </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/hpparvi/ldtk'>ldtk</a></td>
            <td>Python toolkit for calculating stellar limb darkening profiles. </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://arxiv.org/abs/1804.10295'>limb darkening</a></td>
            <td>Limb-darkening and gravity-darkening coefficients for TESS.</td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/rpoleski/MulensModel'>MulensModel</a></td>
            <td>Microlensing Modelling package.</td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/natashabatalha/PandExo'>PandExo</a></td>
            <td>A community tool for transiting exoplanets with HST & JWST. </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/timothydmorton/pymacula'>pymacula</a></td>
            <td>Python wrapper for Macula analytic starspot code.</td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/LucaMalavolta/PyORBIT'>PyOrbit</a></td>
            <td>General toolkit for modeling radial velocity data. </td>
          </tr>
          <tr>
            <td style="width: 15em;"><a
            href='https://github.com/California-Planet-Search/radvel'>radvel</a></td>
            <td>Simultaneously characterize the orbits of exoplanets and the noise induced by stellar activity.</td>
          </tr>
          </table>
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