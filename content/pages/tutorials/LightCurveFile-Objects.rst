LightCurveFile Objects
######################
:save_as: LightCurveFile-Object-Tutorial.html

Understanding LightCurveFile objects
====================================

Learning goals
--------------

In our `LightCurve object tutorial <LightCurve-object-Tutorial.html>`__ we
looked at how to obtain an object of interests light curve from its
``TargetPixelFile`` (TPF; see our `TargetPixelFile
tutorial <Target-Pixel-File-Tutorial.html>`__) using Simple Aperture Photometry
(SAP).

In this tutorial we will demonstrate the difference between a
``TESSLightCurve`` and a ``TESSLightCurveFile``,
and will cover the following, - What is a ``LightCurveFile``. - What is
Pre-search Data Conditioning SAP flux (PSDCSAP). - How can we examine
its ``metadata``. - How we use it to create and examine an objects
light curve.

What is a LightCurveFile object?
--------------------------------

Rather than being generated via a TPF, ``TESSLightCurveFile`` objects
have been pre-generated using NASA’s `Data Processing
Pipeline <https://heasarc.gsfc.nasa.gov/docs/tess/docs/jenkinsSPIE2016-copyright.pdf>`__.
Usually, you will access these files through the `MAST
archive <https://archive.stsci.edu/kepler/data_search/search.php>`__.

What is Pre-search Data Conditioning SAP flux?
----------------------------------------------

``TESSLightCurveFile`` objects have some level of processing (more
details `here <https://arxiv.org/pdf/1207.3093.pdf>`__) and allow you to
access the two kinds of flux; the Simple Aperture Photometry flux (SAP)
flux as discussed in the `LightCurve object
tutorial <LightCurve-object-Tutorial.html>`__, and the Pre-search Data
Conditioning SAP flux (PDCSAP) flux. With PDCSAP flux long term trends
have been removed from the data using so-called Co-trending Basis
Vectors (CBVs). PDCSAP flux is usually cleaner data than the SAP flux
and will have fewer systematic trends.

Imports
-------

This tutorial requires that you import lightkurve

.. code:: ipython3

    %matplotlib inline 
    import lightkurve as lk

Defining terms
--------------

-  Target Pixel File (TPF): A file containing the original CCD pixel
   observations from which light curves are extracted.

-  LightCurve Object: Obtained from a TPF and contains light curve
   information derived using simple aperture photometry.

-  LightCurveFile Object: Obtained from MAST and contains both SAP flux
   and PSDCSAP flux.

-  Cadence: The rate at which TESS photometric observations are stored.

-  Sector: One of TESS’s 27 (to date) observing periods, approximately
   ~27 days in duration.

-  Simple Aperture Photometry (SAP): The act of summing all pixel values
   in a pre-defined aperture as a function of time.

-  Pre-search Data Conditioning SAP flux (PDCSAP) flux : SAP flux from
   which long term trends have been removed using so-called Co-trending
   Basis Vectors (CBVs). PDCSAP flux is usually cleaner data than the
   SAP flux and will have fewer systematic trends.

Downloading the data
--------------------

We can use the
`search_lightcurve() <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.search_lightcurve.html?highlight=search_lightcurve>`__
function to fetch the files from the data archive.

To demonstrate, lets use the `L 98-59
System <https://arxiv.org/pdf/1903.08017.pdf>`__ again, focusing on
planet c.

.. code:: ipython3

    search_result = lk.search_lightcurve('TIC 307210830 c')
    search_result




.. raw:: html

    SearchResult containing 7 data products.
    
    <table id="table140728767307616">
    <thead><tr><th>#</th><th>observation</th><th>author</th><th>target_name</th><th>productFilename</th><th>distance</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 2</td><td>SPOC</td><td>307210830</td><td>tess2018234235059-s0002-0000000307210830-0121-s_lc.fits</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 5</td><td>SPOC</td><td>307210830</td><td>tess2018319095959-s0005-0000000307210830-0125-s_lc.fits</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 8</td><td>SPOC</td><td>307210830</td><td>tess2019032160000-s0008-0000000307210830-0136-s_lc.fits</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 9</td><td>SPOC</td><td>307210830</td><td>tess2019058134432-s0009-0000000307210830-0139-s_lc.fits</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 10</td><td>SPOC</td><td>307210830</td><td>tess2019085135100-s0010-0000000307210830-0140-s_lc.fits</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 11</td><td>SPOC</td><td>307210830</td><td>tess2019112060037-s0011-0000000307210830-0143-s_lc.fits</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 12</td><td>SPOC</td><td>307210830</td><td>tess2019140104343-s0012-0000000307210830-0144-s_lc.fits</td><td>0.0</td></tr>
    </table>



The ``search_lightcurve`` function takes several additional arguments,
such as the ``sector`` number or the ``mission`` name. You can find
examples of its use in the `online
documentation <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.search_lightcurve.html?highlight=search_lightcurve>`__.

Like ``search_targetpixelfile`` the ``search_lightcurve`` function
returns a
`SearchResult <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.SearchResult.html?highlight=searchresult>`__
object which has several convenient operations. For example, we can
select the first data product in the list as follows,

.. code:: ipython3

    search_result[0]




.. raw:: html

    SearchResult containing 1 data products.
    
    <table id="table140728767174584">
    <thead><tr><th>#</th><th>observation</th><th>author</th><th>target_name</th><th>productFilename</th><th>distance</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 2</td><td>SPOC</td><td>307210830</td><td>tess2018234235059-s0002-0000000307210830-0121-s_lc.fits</td><td>0.0</td></tr>
    </table>



We can download this data product using the download() method:

.. code:: ipython3

    lcf = search_result[0].download()

The ``lcf`` variable we have obtained in this way is a
`TessLightCurve <https://lightkurve.github.io/lightkurve/tutorials/1-getting-started/what-are-lightcurve-objects.html?highlight=tesslightcurve>`__
object. This object contains time, flux and flux error information, as
well as a whole lot of data about spacecraft systematics. We can view
all of them by calling the object by itself:

.. code:: ipython3

    lcf




.. raw:: html

    <i>TessLightCurve targetid=307210830 length=18317</i>
    <table id="table140729726451664" class="table-striped table-bordered table-condensed">
    <thead><tr><th>time</th><th>flux</th><th>flux_err</th><th>timecorr</th><th>cadenceno</th><th>centroid_col</th><th>centroid_row</th><th>sap_flux</th><th>sap_flux_err</th><th>sap_bkg</th><th>sap_bkg_err</th><th>pdcsap_flux</th><th>pdcsap_flux_err</th><th>quality</th><th>psf_centr1</th><th>psf_centr1_err</th><th>psf_centr2</th><th>psf_centr2_err</th><th>mom_centr1</th><th>mom_centr1_err</th><th>mom_centr2</th><th>mom_centr2_err</th><th>pos_corr1</th><th>pos_corr2</th></tr></thead>
    <thead><tr><th></th><th>electron / s</th><th>electron / s</th><th>d</th><th></th><th>pix</th><th>pix</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th></th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th></tr></thead>
    <thead><tr><th>object</th><th>float32</th><th>float32</th><th>float32</th><th>int32</th><th>float64</th><th>float64</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>int32</th><th>float64</th><th>float32</th><th>float64</th><th>float32</th><th>float64</th><th>float32</th><th>float64</th><th>float32</th><th>float32</th><th>float32</th></tr></thead>
    <tr><td>1354.1088231272427</td><td>2.4311873e+04</td><td>1.8769577e+01</td><td>-8.0589490e-04</td><td>91191</td><td>664.10903</td><td>338.97642</td><td>2.1566352e+04</td><td>1.6472113e+01</td><td>1.3385229e+03</td><td>3.5451272e+00</td><td>2.4311873e+04</td><td>1.8769577e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.10903</td><td>5.8178976e-04</td><td>338.97642</td><td>6.0455920e-04</td><td>4.8032869e-02</td><td>1.4890091e-01</td></tr>
    <tr><td>1354.1102119888994</td><td>2.4297582e+04</td><td>1.8773235e+01</td><td>-8.0592179e-04</td><td>91192</td><td>664.12611</td><td>338.96839</td><td>2.1563889e+04</td><td>1.6475323e+01</td><td>1.3444882e+03</td><td>3.5518360e+00</td><td>2.4297582e+04</td><td>1.8773235e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.12611</td><td>5.8167754e-04</td><td>338.96839</td><td>6.0535187e-04</td><td>6.5402389e-02</td><td>1.3844931e-01</td></tr>
    <tr><td>1354.112989712153</td><td>2.4282812e+04</td><td>1.8741255e+01</td><td>-8.0597564e-04</td><td>91194</td><td>664.10668</td><td>338.96049</td><td>2.1475160e+04</td><td>1.6447256e+01</td><td>1.3468779e+03</td><td>3.5524495e+00</td><td>2.4282812e+04</td><td>1.8741255e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.10668</td><td>5.8500003e-04</td><td>338.96049</td><td>6.0745567e-04</td><td>4.0374711e-02</td><td>1.3017291e-01</td></tr>
    <tr><td>1354.1143785738097</td><td>2.4275164e+04</td><td>1.8781441e+01</td><td>-8.0600253e-04</td><td>91195</td><td>664.14148</td><td>338.98328</td><td>2.1583307e+04</td><td>1.6482523e+01</td><td>1.3438405e+03</td><td>3.5524592e+00</td><td>2.4275164e+04</td><td>1.8781441e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.14148</td><td>5.8221997e-04</td><td>338.98328</td><td>6.0431601e-04</td><td>8.0888584e-02</td><td>1.5741505e-01</td></tr>
    <tr><td>1354.1157674355243</td><td>2.4288371e+04</td><td>1.8776447e+01</td><td>-8.0602936e-04</td><td>91196</td><td>664.13548</td><td>338.97358</td><td>2.1575641e+04</td><td>1.6478142e+01</td><td>1.3419084e+03</td><td>3.5480881e+00</td><td>2.4288371e+04</td><td>1.8776447e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.13548</td><td>5.8233330e-04</td><td>338.97358</td><td>6.0483697e-04</td><td>7.4183472e-02</td><td>1.4472328e-01</td></tr>
    <tr><td>1354.1171562971804</td><td>2.4280523e+04</td><td>1.8768578e+01</td><td>-8.0605625e-04</td><td>91197</td><td>664.13351</td><td>338.97214</td><td>2.1563102e+04</td><td>1.6471235e+01</td><td>1.3378163e+03</td><td>3.5436206e+00</td><td>2.4280523e+04</td><td>1.8768578e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.13351</td><td>5.8274117e-04</td><td>338.97214</td><td>6.0512009e-04</td><td>7.1515344e-02</td><td>1.4336312e-01</td></tr>
    <tr><td>1354.1185451588947</td><td>2.4286711e+04</td><td>1.8765480e+01</td><td>-8.0608309e-04</td><td>91198</td><td>664.12517</td><td>338.96675</td><td>2.1552936e+04</td><td>1.6468515e+01</td><td>1.3372028e+03</td><td>3.5442295e+00</td><td>2.4286711e+04</td><td>1.8765480e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.12517</td><td>5.8198441e-04</td><td>338.96675</td><td>6.0517463e-04</td><td>6.5269679e-02</td><td>1.3618952e-01</td></tr>
    <tr><td>1354.1199340205515</td><td>2.4255619e+04</td><td>1.8757978e+01</td><td>-8.0610998e-04</td><td>91199</td><td>664.13023</td><td>338.96995</td><td>2.1532902e+04</td><td>1.6461933e+01</td><td>1.3415085e+03</td><td>3.5453105e+00</td><td>2.4255619e+04</td><td>1.8757978e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.13023</td><td>5.8275240e-04</td><td>338.96995</td><td>6.0552283e-04</td><td>6.8680957e-02</td><td>1.3969450e-01</td></tr>
    <tr><td>1354.1213228822667</td><td>2.4262840e+04</td><td>1.8758078e+01</td><td>-8.0613681e-04</td><td>91200</td><td>664.12622</td><td>338.96554</td><td>2.1533828e+04</td><td>1.6462021e+01</td><td>1.3382404e+03</td><td>3.5454845e+00</td><td>2.4262840e+04</td><td>1.8758078e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.12622</td><td>5.8211992e-04</td><td>338.96554</td><td>6.0527271e-04</td><td>6.5827116e-02</td><td>1.3609535e-01</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>1381.5001032523294</td><td>2.4288518e+04</td><td>1.9145361e+01</td><td>-1.1857213e-03</td><td>110913</td><td>664.07445</td><td>338.85133</td><td>2.1262494e+04</td><td>1.6801899e+01</td><td>2.1153037e+03</td><td>4.2768788e+00</td><td>2.4288518e+04</td><td>1.9145361e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07445</td><td>6.0456968e-04</td><td>338.85133</td><td>6.3469319e-04</td><td>6.7313453e-03</td><td>-1.7380530e-02</td></tr>
    <tr><td>1381.5014921207378</td><td>2.4314963e+04</td><td>1.9157202e+01</td><td>-1.1857414e-03</td><td>110914</td><td>664.07975</td><td>338.84913</td><td>2.1289830e+04</td><td>1.6812288e+01</td><td>2.1122083e+03</td><td>4.2748408e+00</td><td>2.4314963e+04</td><td>1.9157202e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07975</td><td>6.0464692e-04</td><td>338.84913</td><td>6.3474779e-04</td><td>1.2294311e-02</td><td>-1.9028442e-02</td></tr>
    <tr><td>1381.5028809891458</td><td>2.4287336e+04</td><td>1.9145287e+01</td><td>-1.1857615e-03</td><td>110915</td><td>664.07908</td><td>338.85137</td><td>2.1266350e+04</td><td>1.6801832e+01</td><td>2.1092537e+03</td><td>4.2716589e+00</td><td>2.4287336e+04</td><td>1.9145287e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07908</td><td>6.0521072e-04</td><td>338.85137</td><td>6.3506985e-04</td><td>1.1281053e-02</td><td>-1.7392185e-02</td></tr>
    <tr><td>1381.5042698574382</td><td>2.4250791e+04</td><td>1.9129375e+01</td><td>-1.1857818e-03</td><td>110916</td><td>664.07296</td><td>338.85550</td><td>2.1234850e+04</td><td>1.6787870e+01</td><td>2.0995103e+03</td><td>4.2670422e+00</td><td>2.4250791e+04</td><td>1.9129375e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07296</td><td>6.0523918e-04</td><td>338.85550</td><td>6.3468731e-04</td><td>3.6670761e-03</td><td>-1.0083861e-02</td></tr>
    <tr><td>1381.5056587258466</td><td>2.4272904e+04</td><td>1.9130596e+01</td><td>-1.1858019e-03</td><td>110917</td><td>664.07822</td><td>338.84684</td><td>2.1244951e+04</td><td>1.6788940e+01</td><td>2.0982610e+03</td><td>4.2620702e+00</td><td>2.4272904e+04</td><td>1.9130596e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07822</td><td>6.0487830e-04</td><td>338.84684</td><td>6.3467148e-04</td><td>1.0049758e-02</td><td>-2.2052733e-02</td></tr>
    <tr><td>1381.5070475942555</td><td>2.4244773e+04</td><td>1.9113134e+01</td><td>-1.1858221e-03</td><td>110918</td><td>664.07699</td><td>338.84420</td><td>2.1210760e+04</td><td>1.6773617e+01</td><td>2.0926931e+03</td><td>4.2577090e+00</td><td>2.4244773e+04</td><td>1.9113134e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07699</td><td>6.0498924e-04</td><td>338.84420</td><td>6.3551613e-04</td><td>7.6570297e-03</td><td>-2.6143335e-02</td></tr>
    <tr><td>1381.508436462548</td><td>2.4274957e+04</td><td>1.9118402e+01</td><td>-1.1858423e-03</td><td>110919</td><td>664.07860</td><td>338.84214</td><td>2.1231014e+04</td><td>1.6778240e+01</td><td>2.0832832e+03</td><td>4.2526455e+00</td><td>2.4274957e+04</td><td>1.9118402e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07860</td><td>6.0521363e-04</td><td>338.84214</td><td>6.3519127e-04</td><td>1.0699908e-02</td><td>-3.0003805e-02</td></tr>
    <tr><td>1381.5098253309563</td><td>2.4274902e+04</td><td>1.9122919e+01</td><td>-1.1858625e-03</td><td>110920</td><td>664.07231</td><td>338.85137</td><td>2.1250465e+04</td><td>1.6782204e+01</td><td>2.0831892e+03</td><td>4.2515340e+00</td><td>2.4274902e+04</td><td>1.9122919e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07231</td><td>6.0427783e-04</td><td>338.85137</td><td>6.3426507e-04</td><td>4.3808916e-03</td><td>-1.5397585e-02</td></tr>
    <tr><td>1381.5112141992488</td><td>2.4265334e+04</td><td>1.9115648e+01</td><td>-1.1858827e-03</td><td>110921</td><td>664.08214</td><td>338.84521</td><td>2.1236355e+04</td><td>1.6775822e+01</td><td>2.0772075e+03</td><td>4.2467227e+00</td><td>2.4265334e+04</td><td>1.9115648e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.08214</td><td>6.0488580e-04</td><td>338.84521</td><td>6.3436205e-04</td><td>1.4993464e-02</td><td>-2.5431424e-02</td></tr>
    <tr><td>1381.5126030676577</td><td>2.4296789e+04</td><td>1.9121765e+01</td><td>-1.1859029e-03</td><td>110922</td><td>664.07292</td><td>338.84971</td><td>2.1265840e+04</td><td>1.6781191e+01</td><td>2.0722200e+03</td><td>4.2412267e+00</td><td>2.4296789e+04</td><td>1.9121765e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07292</td><td>6.0415227e-04</td><td>338.84971</td><td>6.3310139e-04</td><td>4.4403672e-03</td><td>-1.8668674e-02</td></tr>
    </table>



Note that unlike the table generated via a ``LightCurve Object``, this
table contains the SAP flux and PDCSAP flux!

Plotting the light curve
------------------------

Lets now plot the light curve up for the object.

.. code:: ipython3

    lcf.plot();



.. image:: images/LightCurveFile-Objects_files/LightCurveFile-Objects_17_0.png
    :alt: SPOC lightcurve


SAP and PDCSAP light curves
~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, a
`TESSLightCurveFiles <https://lightkurve.github.io/lightkurve/tutorials/1-getting-started/what-are-lightcurve-objects.html?highlight=tesslightcurve>`__
will set the PDCSAP flux to its ``.flux`` property.

To compare the PDCSAP and the SAP flux, we can use the ``column``
keyword while plotting.

**Note**: alternatively, you can replace the ``flux`` column with the
``sap_flux`` column by using \`lcf.flux = lcf[‘sap_flux’]

.. code:: ipython3

    ax = lcf.plot(label='PDCSAP Flux', normalize=True)
    lcf.plot(column='sap_flux', normalize=True, label='SAP Flux', ax=ax);



.. image:: images/LightCurveFile-Objects_files/LightCurveFile-Objects_19_0.png
    :alt: Simple and corrected lightcurve comparison


In brief:

-  The SAP light curve is calculated by summing together the brightness
   of pixels that fall within an aperture set by the *TESS* mission.
   This is often referred to as the *optimal aperture*, but in spite of
   its name can sometimes be improved upon! Because the SAP light curve
   is a sum of the brightness in chosen pixels, it is still subject to
   systematic artifacts of the mission.

-  The PDCSAP light curve is subject to more treatment than the SAP
   light curve, and is specifically intended for detecting planets. The
   PDCSAP pipeline attempts to remove systematic artifacts while keeping
   planetary transits intact.

Looking at the Figure we made above, you can see that the SAP light
curve has a long-term change in brightness that has been removed in the
PDCSAP light curve, while keeping the transits at the same depth. For
most inspections, a PDCSAP light curve is what you want to use, but when
looking at astronomical phenomena that aren’t planets (e.g. long-term
variability), the SAP flux may be preferred.

You can switch between fluxes using the following commands,

::

   pdcsap = lcf.flux

   sap =lcf.sap_flux

For now, let’s continue to use the PDCSAP flux only. Because this is the
default .flux property of our light curve object, we don’t need to
change anything.

Note
^^^^

The ``plot()`` methods in *Lightkurve* always return a
`Matplotlib <https://matplotlib.org/>`__ object. This is useful because
it lets us manipulate the plot using standard Matplotlib functions. For
example, we can set the title as follow:

.. code:: ipython3

    ax = lcf.plot() 
    ax.set_title("PDCSAP light curve of  L 98-59")




.. parsed-literal::

    Text(0.5, 1.0, 'PDCSAP light curve of  L 98-59')




.. image:: images/LightCurveFile-Objects_files/LightCurveFile-Objects_21_1.png
    :alt: PDCSAP lightcurve


Now lets fold and bin our data to look at the transit as we did in the
`LightCurve object tutorial <LightCurve-object-Tutorial.html>`__. Remember the
``lcf.flux`` default is the PDCSAP flux this time!

.. code:: ipython3

    lcf.remove_nans().flatten(window_length=401).fold(period=3.690621,  epoch_time=1367.2755).bin(time_bin_size=0.025).plot();



.. image:: images/LightCurveFile-Objects_files/LightCurveFile-Objects_23_0.png
    :alt: Flattened lightcurve folded on transit period


Metadata
--------

You can check the meta data and the CDPP noise metric of the
``TESSLightCurveFile`` as we have in the past.

.. code:: ipython3

    lcf.meta




.. parsed-literal::

    {'inherit': True,
     'extname': 'PRIMARY',
     'extver': 1,
     'simdata': False,
     'telescop': 'TESS',
     'instrume': 'TESS Photometer',
     'object': 'TIC 307210830',
     'ticid': 307210830,
     'radesys': 'ICRS',
     'ra_obj': 124.5319,
     'dec_obj': -68.313,
     'equinox': 2000.0,
     'exposure': 21.710393585867,
     'timeref': 'SOLARSYSTEM',
     'tassign': 'SPACECRAFT',
     'timesys': 'TDB',
     'bjdrefi': 2457000,
     'bjdreff': 0.0,
     'timeunit': 'd',
     'telapse': 27.412113113468,
     'livetime': 21.71039358586663,
     'tstart': 1354.101978098092,
     'tstop': 1381.514471377755,
     'date-obs': '2018-08-23T14:25:41.724Z',
     'date-end': '2018-09-20T00:19:41.143Z',
     'deadc': 0.792,
     'timepixr': 0.5,
     'tierrela': 1.16e-05,
     'int_time': 1.98,
     'readtime': 0.02,
     'frametim': 2.0,
     'num_frm': 60,
     'timedel': 0.001388888888888889,
     'backapp': True,
     'deadapp': True,
     'vignapp': True,
     'gaina': 5.300000190734863,
     'gainb': 5.179999828338623,
     'gainc': 5.269999980926514,
     'gaind': 5.190000057220459,
     'readnoia': 10.017000198364258,
     'readnoib': 7.407399654388428,
     'readnoic': 7.85230016708374,
     'readnoid': 9.964799880981445,
     'nreadout': 48,
     'fxdoff': 209700,
     'cdpp0_5': 264.31433105,
     'cdpp1_0': 202.23320007,
     'cdpp2_0': 159.35473633,
     'crowdsap': 0.99806839,
     'flfrcsap': 0.87759632,
     'nspsddet': 0,
     'nspsdcor': 0,
     'pdcvar': 0.9957757182968056,
     'pdcmethd': 'msMAP',
     'numband': 3,
     'fittype1': 'reducedRobust',
     'pr_good1': 0.9786046743392944,
     'pr_wght1': 0.0,
     'fittype2': 'prior',
     'pr_good2': 0.06772279739379883,
     'pr_wght2': 5.394961833953857,
     'fittype3': 'prior',
     'pr_good3': 0.6207972764968872,
     'pr_wght3': 49.4542121887207,
     'pdc_tot': 0.8734737634658813,
     'pdc_totp': 54.40318298339844,
     'pdc_cor': 0.999976396560669,
     'pdc_corp': 76.24014282226562,
     'pdc_var': 0.9333910942077637,
     'pdc_varp': 23.97138214111328,
     'pdc_noi': 0.5902431607246399,
     'pdc_noip': 59.09120559692383,
     'pdc_ept': 1.0,
     'pdc_eptp': 53.693321228027344,
     'checksum': 'ETQJHSNGESNGESNG',
     'tmofst43': 1.0399999618530273,
     'meanblca': 6664,
     'meanblcb': 6554,
     'meanblcc': 6593,
     'meanblcd': 6169,
     'simple': True,
     'bitpix': 8,
     'naxis': 0,
     'extend': True,
     'nextend': 2,
     'origin': 'NASA/Ames',
     'date': '2018-10-06',
     'creator': '4612 LightCurveExporterPipelineModule',
     'procver': 'spoc-3.3.37-20181001',
     'filever': '1.0',
     'timversn': 'OGIP/93-003',
     'data_rel': 2,
     'sector': 2,
     'camera': 4,
     'ccd': 3,
     'pxtable': 129,
     'pmra': 96.4716,
     'pmdec': -340.083,
     'pmtotal': 353.50136703,
     'tessmag': 9.39299965,
     'teff': 3469.0,
     'logg': 4.94010019,
     'mh': None,
     'radius': 0.31299999,
     'ticver': 7,
     'crmiten': True,
     'crblksz': 10,
     'crspoc': False,
     'label': 'TIC 307210830',
     'mission': 'TESS',
     'ra': 124.5319,
     'dec': -68.313,
     'filename': '/Users/rhounsel/.lightkurve-cache/mastDownload/TESS/tess2018234235059-s0002-0000000307210830-0121-s/tess2018234235059-s0002-0000000307210830-0121-s_lc.fits',
     'targetid': 307210830,
     'quality_bitmask': 'default',
     'quality_mask': array([False, False, False, ...,  True,  True,  True])}



.. code:: ipython3

    lcf.mission




.. parsed-literal::

    'TESS'



.. code:: ipython3

    lcf.sector




.. parsed-literal::

    2



.. code:: ipython3

    lcf.estimate_cdpp()




.. math::

    218.15446 \; \mathrm{ppm}



Congratulations! You have now learnt how to work with LightCurveFiles.
