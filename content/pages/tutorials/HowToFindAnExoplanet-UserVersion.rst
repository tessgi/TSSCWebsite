HowToFindAnExoplanet-UserVersion
################################
:save_as: HowToFindAnExoplanet-UserVersion.html

How to find an Exoplanet with TESS data
=======================================

When a planet passes in front of its host star, from a certain view
point, it causes the light of that star to dim. This is known as a
transit.

.. image:: images/mission/transit_white.png
    :alt: Exoplanet transit graphic

Many space missions have been specifically designed to detect planets
using the transit method. One such mission is the `Transiting Exoplanet
Survey Satellite (TESS) <https://heasarc.gsfc.nasa.gov/docs/tess/>`__.

*TESS* is a NASA-sponsored Astrophysics Explorer-class mission that is
performing a near all-sky survey to search for planets transiting nearby
stars. The mission observes from a unique elliptical high Earth orbit
(HEO) that provides an unobstructed view of its field to obtain
continuous light curves and a more stable platform for precise
photometry than a low Earth orbit.

.. image:: images/mission/tess_lava_planet_rotated.jpg
    :alt: TESS glamour image

*TESS* is equipped with four CCD cameras that have adjacent
field-of-views to produce a 4 x 1 array, or ‘observing Sector’, yielding
a combined field-of-view of 96 x 24 degrees, as illustrated below.

.. image:: images/mission/tess_observingsectorschematic_Winnpresentation.jpg
    :alt: TESS prime mission observing sectors

Each hemisphere is split into these observing Sectors, and each Sector
is observed for ~27 days. Since 2018, TESS has observed approximately
80% of the sky, mapping both the northern and southern hemispheres, and
detecting thousands of planet candidates.

Data from the *TESS* mission are publicly available from the `Mikulski
Archive for Space Telescopes
(MAST) <https://archive.stsci.edu/missions-and-data/tess>`__. The main
data products collected by the *TESS* mission are described below:

-  `Full Frame Images
   (FFIs) <https://heasarc.gsfc.nasa.gov/docs/tess/data-products.html#full-frame-images>`__:
   The full sector images, with a cadence of 30-min (years 1 & 2) or
   10-min (years 3 & 4).
-  `Target Pixel Files
   (TPFs) <https://heasarc.gsfc.nasa.gov/docs/tess/data-products.html#target-pixel-files-tpfs>`__:
   Postage stamp cut outs from the FFIs, focused on a selected target of
   interest. Each stamp has a cadence of 2-min or 20-sec.
-  `Light Curve Files
   (LCFs) <https://heasarc.gsfc.nasa.gov/docs/tess/data-products.html#light-curve-files>`__:
   The time series data produced for each 2-min or 20-sec TPF object.

To learn more about the *TESS* mission and its data products, please
visit the `TESS GI
pages <https://heasarc.gsfc.nasa.gov/docs/tess/data-products.html>`__.


Download the notebook
=====================

If you would like to download a copy of this notebook you can do so by clicking the link below

.. raw:: html

   <p><a class="reference download internal" href="https://tessgi.github.io/TessGiWebsite/docs/tutorials/HowToFindAnExoplanet-UserVersion.ipynb">
   <tt class="xref download docutils literal">
   DOWNLOAD
   </tt></a><p>

Learning Goals
--------------

In this tutorial, we will teach the user how to access, analyze, and
manipulate data from the *TESS* mission (this can also be applied to
*Kepler* & *K2*). We will be utilizing a
`Python <https://www.python.org>`__ package called
`Lightkurve <https://lightkurve.github.io/lightkurve/index.html>`__ which offers a
user-friendly way to analyze time series data on the brightness of
planets, stars, and galaxies. The package is focused on supporting
science with NASA’s *Kepler* and *TESS* space telescopes but can equally
be used to analyze light curves obtained by your backyard telescope.

This tutorial assumes a basic knowledge of python and astronomy, and
will walk the user through several of the concepts outlined below,

-  How to use *Lightkurve* to access the various data products and
   create time series.
-  How to account for instrumental and noise effects within your data.
-  How to recover a planet transit from your data.

Imports
-------

This tutorial requires the use of specific packages: -
`Lightkurve <https://lightkurve.github.io/lightkurve/index.html>`__ to work with
*TESS* data (v2.0.1) - `Matplotlib <https://matplotlib.org/>`__ for
plotting. - `Numpy <https://numpy.org>`__ for manipulating the data.

.. code:: ipython3

    import lightkurve as lk
    import numpy as np
    import matplotlib.pyplot as plt
    %matplotlib inline

First time users
~~~~~~~~~~~~~~~~

If you are not experienced with *Python*, or cannot download
*Lightkurve*, you can run this notebook as a `Colab
notebook <https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index>`__.
Colaboratory allows users to write and execute *Python* in your browser
with zero configuration required.

All you need is a Google account and to copy and paste in the following
command at the top of your colab notebook:

``!pip install lightkurve --quiet``

This downloads the *Lightkurve* package.

1. How to use *Lightkurve* to access the various data products and create a time series
---------------------------------------------------------------------------------------

You can search for the various data products for *TESS* using the
following *Lightkurve* functions.

-  To look for your object in a full frame image:
   ```search_tesscut()`` <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.search_tesscut.html?highlight=search_tesscut>`__

-  To look for target pixel files:
   ```search_targetpixelfile()`` <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.search_targetpixelfile.html?highlight=search_targetpixelfile>`__

-  To obtain light curve files for your object of interest:
   ```search_lightcurve()`` <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.search_lightcurve.html?highlight=search_lightcurve>`__

In this tutorial, we will be examining a nearby, bright target `Pi
Mensae <https://exoplanets.nasa.gov/exoplanet-catalog/7271/pi-mensae-c/>`__
(TIC ID 261136679), around which *TESS* scientists discovered a short
period planet candidate on a 6.27 day orbit. See the ApJ paper by `Huang
et al
(2018) <https://iopscience.iop.org/article/10.3847/2041-8213/aaef91/pdf>`__
for more details.

1.1 Accessing the data products
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let’s go through each one of the above functions and see what data is
available.

.. code:: ipython3

    search_ffi = lk.search_tesscut('Pi Mensae')
    search_tpf = lk.search_targetpixelfile('Pi Mensae')
    search_lcf = lk.search_lightcurve('Pi Mensae')

.. code:: ipython3

    search_ffi




.. raw:: html

    SearchResult containing 13 data products.
    
    <table id="table140397123000208">
    <thead><tr><th>#</th><th>mission</th><th>year</th><th>author</th><th>exptime</th><th>target_name</th><th>distance</th></tr></thead>
    <thead><tr><th></th><th></th><th></th><th></th><th>s</th><th></th><th>arcsec</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 04</td><td>2018</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 11</td><td>2019</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 12</td><td>2019</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 13</td><td>2019</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 27</td><td>2020</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>7</td><td>TESS Sector 28</td><td>2020</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>8</td><td>TESS Sector 31</td><td>2020</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>9</td><td>TESS Sector 34</td><td>2021</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>10</td><td>TESS Sector 35</td><td>2021</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>11</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>Pi Mensae</td><td>0.0</td></tr>
    <tr><td>12</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>Pi Mensae</td><td>0.0</td></tr>
    </table>



The above table provides several important pieces of information. - The
sector in which the object was observed. - The year in which the object
was observed. - The author of the data. This has multiple options, and
each is a hyperlink that when clicked will provide you with more
information. - The cadence of the observation. - The name of the target.
- The distance of the observation from your target of interest. This is
useful if you conduct a cone search around your objects co-ordinates.

The table above indicates that our object was observed in multiple
Sectors. Note that in Sectors 1 - 13 (2018 & 2019) that the cadence of
the FFI data was 30-min, but in Sectors 27 and above (2020 & 2021) it is
10-min.

Let’s see if any other data exists - i.e., was it observed as a target
of interest and does it have a Target Pixel File.

.. code:: ipython3

    search_tpf




.. raw:: html

    SearchResult containing 30 data products.
    
    <table id="table140395774407056">
    <thead><tr><th>#</th><th>mission</th><th>year</th><th>author</th><th>exptime</th><th>target_name</th><th>distance</th></tr></thead>
    <thead><tr><th></th><th></th><th></th><th></th><th>s</th><th></th><th>arcsec</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 04</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 04</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 11</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>7</td><td>TESS Sector 11</td><td>2019</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>8</td><td>TESS Sector 12</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>9</td><td>TESS Sector 12</td><td>2019</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>20</td><td>TESS Sector 31</td><td>2020</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>600</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>21</td><td>TESS Sector 34</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>22</td><td>TESS Sector 34</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>23</td><td>TESS Sector 34</td><td>2021</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>600</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>24</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>25</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>26</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>600</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>27</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>28</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>29</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>600</td><td>261136679</td><td>0.0</td></tr>
    </table>
    Length = 30 rows



Great! Our object was observed as a target of interest and has 2-min and
20-sec cadenced data. This means that there should be light curve files
already on the archive. Let’s check those out.

.. code:: ipython3

    search_lcf




.. raw:: html

    SearchResult containing 41 data products.
    
    <table id="table140395774508624">
    <thead><tr><th>#</th><th>mission</th><th>year</th><th>author</th><th>exptime</th><th>target_name</th><th>distance</th></tr></thead>
    <thead><tr><th></th><th></th><th></th><th></th><th>s</th><th></th><th>arcsec</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/qlp'>QLP</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tasoc'>TASOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tasoc'>TASOC</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 04</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 04</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>7</td><td>TESS Sector 04</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/qlp'>QLP</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>8</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>9</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>31</td><td>TESS Sector 31</td><td>2020</td><td><a href='https://archive.stsci.edu/hlsp/qlp'>QLP</a></td><td>600</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>32</td><td>TESS Sector 34</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>33</td><td>TESS Sector 34</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>34</td><td>TESS Sector 34</td><td>2021</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>600</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>35</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>36</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>37</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>600</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>38</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>39</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>40</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>600</td><td>261136679</td><td>0.0</td></tr>
    </table>
    Length = 41 rows



Wonderful! Light curves for our object of interest have already been
created.

1.2 Creating a light curve using a Light Curve File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now on to getting the light curve for our object of interest. From the
above table, it looks like there are multiple authors for our target.
For this tutorial, let’s stick to “SPOC” data products which have a
2-min cadence. We can return only these results using the following
commands.

.. code:: ipython3

    search_lcf_refined = lk.search_lightcurve('Pi Mensae', author="SPOC", exptime=120)
    search_lcf_refined 




.. raw:: html

    SearchResult containing 12 data products.
    
    <table id="table140396326482000">
    <thead><tr><th>#</th><th>mission</th><th>year</th><th>author</th><th>exptime</th><th>target_name</th><th>distance</th></tr></thead>
    <thead><tr><th></th><th></th><th></th><th></th><th>s</th><th></th><th>arcsec</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 04</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 11</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 12</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 13</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 27</td><td>2020</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>7</td><td>TESS Sector 28</td><td>2020</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>8</td><td>TESS Sector 31</td><td>2020</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>9</td><td>TESS Sector 34</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>10</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    <tr><td>11</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>261136679</td><td>0.0</td></tr>
    </table>



We now see 11 search results. Let’s download these and see what the
light curve looks like.

.. code:: ipython3

    lcf = search_lcf_refined.download_all()

.. code:: ipython3

    lcf




.. parsed-literal::

    LightCurveCollection of 12 objects:
        0: <TessLightCurve LABEL="TIC 261136679" SECTOR=1 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        1: <TessLightCurve LABEL="TIC 261136679" SECTOR=4 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        2: <TessLightCurve LABEL="TIC 261136679" SECTOR=8 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        3: <TessLightCurve LABEL="TIC 261136679" SECTOR=11 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        4: <TessLightCurve LABEL="TIC 261136679" SECTOR=12 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        5: <TessLightCurve LABEL="TIC 261136679" SECTOR=13 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        6: <TessLightCurve LABEL="TIC 261136679" SECTOR=27 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        7: <TessLightCurve LABEL="TIC 261136679" SECTOR=28 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        8: <TessLightCurve LABEL="TIC 261136679" SECTOR=31 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        9: <TessLightCurve LABEL="TIC 261136679" SECTOR=34 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        10: <TessLightCurve LABEL="TIC 261136679" SECTOR=38 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        11: <TessLightCurve LABEL="TIC 261136679" SECTOR=39 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>



The above indicates that we have downloaded the light curves for each
Sector and stored the data in arrays. You can look at the data for a
specific Sector by specifying an array number as indicated below. This
displays the data for Sector 1 as a table.

.. code:: ipython3

    lcf[0]




.. raw:: html

    <i>TessLightCurve length=18279 LABEL=&quot;TIC 261136679&quot; SECTOR=1 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux</i>
    <table id="table140397679045584" class="table-striped table-bordered table-condensed">
    <thead><tr><th>time</th><th>flux</th><th>flux_err</th><th>timecorr</th><th>cadenceno</th><th>centroid_col</th><th>centroid_row</th><th>sap_flux</th><th>sap_flux_err</th><th>sap_bkg</th><th>sap_bkg_err</th><th>pdcsap_flux</th><th>pdcsap_flux_err</th><th>quality</th><th>psf_centr1</th><th>psf_centr1_err</th><th>psf_centr2</th><th>psf_centr2_err</th><th>mom_centr1</th><th>mom_centr1_err</th><th>mom_centr2</th><th>mom_centr2_err</th><th>pos_corr1</th><th>pos_corr2</th></tr></thead>
    <thead><tr><th></th><th>electron / s</th><th>electron / s</th><th>d</th><th></th><th>pix</th><th>pix</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th></th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th></tr></thead>
    <thead><tr><th>object</th><th>float32</th><th>float32</th><th>float32</th><th>int32</th><th>float64</th><th>float64</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>int32</th><th>float64</th><th>float32</th><th>float64</th><th>float32</th><th>float64</th><th>float32</th><th>float64</th><th>float32</th><th>float32</th><th>float32</th></tr></thead>
    <tr><td>1325.2969604950604</td><td>1.4641956e+06</td><td>1.3036719e+02</td><td>1.2319778e-03</td><td>70445</td><td>1630.67624</td><td>260.67540</td><td>1.4354926e+06</td><td>1.2776145e+02</td><td>3.9114688e+03</td><td>1.5351995e+01</td><td>1.4641956e+06</td><td>1.3036719e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.67624</td><td>8.4099076e-05</td><td>260.67540</td><td>1.3968609e-04</td><td>9.0913408e-02</td><td>-7.2966635e-02</td></tr>
    <tr><td>1325.2983493645327</td><td>1.4643365e+06</td><td>1.3035809e+02</td><td>1.2319590e-03</td><td>70446</td><td>1630.64880</td><td>260.63392</td><td>1.4357199e+06</td><td>1.2775254e+02</td><td>3.8596919e+03</td><td>1.5269516e+01</td><td>1.4643365e+06</td><td>1.3035809e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64880</td><td>8.4054744e-05</td><td>260.63392</td><td>1.3961994e-04</td><td>6.2022530e-02</td><td>-1.0871942e-01</td></tr>
    <tr><td>1325.299738234005</td><td>1.4643485e+06</td><td>1.3035931e+02</td><td>1.2319401e-03</td><td>70447</td><td>1630.64806</td><td>260.62840</td><td>1.4356588e+06</td><td>1.2775373e+02</td><td>3.8692920e+03</td><td>1.5291610e+01</td><td>1.4643485e+06</td><td>1.3035931e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64806</td><td>8.4062471e-05</td><td>260.62840</td><td>1.3959571e-04</td><td>6.1673984e-02</td><td>-1.1394957e-01</td></tr>
    <tr><td>1325.301127103477</td><td>1.4643674e+06</td><td>1.3035008e+02</td><td>1.2319213e-03</td><td>70448</td><td>1630.64752</td><td>260.61434</td><td>1.4356190e+06</td><td>1.2774468e+02</td><td>3.8398132e+03</td><td>1.5262703e+01</td><td>1.4643674e+06</td><td>1.3035008e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64752</td><td>8.4045743e-05</td><td>260.61434</td><td>1.3958366e-04</td><td>6.0909923e-02</td><td>-1.2573890e-01</td></tr>
    <tr><td>1325.3025159730657</td><td>1.4642560e+06</td><td>1.3034836e+02</td><td>1.2319025e-03</td><td>70449</td><td>1630.64057</td><td>260.61412</td><td>1.4355810e+06</td><td>1.2774299e+02</td><td>3.8384204e+03</td><td>1.5262712e+01</td><td>1.4642560e+06</td><td>1.3034836e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64057</td><td>8.4043444e-05</td><td>260.61412</td><td>1.3952980e-04</td><td>5.3837594e-02</td><td>-1.2532526e-01</td></tr>
    <tr><td>1325.303904842538</td><td>1.4644681e+06</td><td>1.3035623e+02</td><td>1.2318837e-03</td><td>70450</td><td>1630.63971</td><td>260.61326</td><td>1.4358005e+06</td><td>1.2775071e+02</td><td>3.8069717e+03</td><td>1.5240330e+01</td><td>1.4644681e+06</td><td>1.3035623e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.63971</td><td>8.4056861e-05</td><td>260.61326</td><td>1.3949080e-04</td><td>5.2977830e-02</td><td>-1.2562653e-01</td></tr>
    <tr><td>1325.3052937121265</td><td>1.4643586e+06</td><td>1.3035381e+02</td><td>1.2318649e-03</td><td>70451</td><td>1630.64385</td><td>260.60708</td><td>1.4356219e+06</td><td>1.2774834e+02</td><td>3.8431169e+03</td><td>1.5283619e+01</td><td>1.4643586e+06</td><td>1.3035381e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64385</td><td>8.4062158e-05</td><td>260.60708</td><td>1.3951714e-04</td><td>5.7222184e-02</td><td>-1.3051888e-01</td></tr>
    <tr><td>1325.3066825815986</td><td>1.4643564e+06</td><td>1.3035527e+02</td><td>1.2318461e-03</td><td>70452</td><td>1630.64220</td><td>260.61215</td><td>1.4356771e+06</td><td>1.2774977e+02</td><td>3.8419392e+03</td><td>1.5270525e+01</td><td>1.4643564e+06</td><td>1.3035527e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64220</td><td>8.4041087e-05</td><td>260.61215</td><td>1.3955019e-04</td><td>5.5443291e-02</td><td>-1.2712292e-01</td></tr>
    <tr><td>1325.3080714511873</td><td>1.4645452e+06</td><td>1.3035765e+02</td><td>1.2318273e-03</td><td>70453</td><td>1630.63883</td><td>260.60831</td><td>1.4357862e+06</td><td>1.2775210e+02</td><td>3.8407632e+03</td><td>1.5274895e+01</td><td>1.4645452e+06</td><td>1.3035765e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.63883</td><td>8.4034349e-05</td><td>260.60831</td><td>1.3950600e-04</td><td>5.1877767e-02</td><td>-1.2947108e-01</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>1353.1645661947705</td><td>1.4646795e+06</td><td>1.3039951e+02</td><td>7.9329044e-04</td><td>90510</td><td>1630.64438</td><td>260.73540</td><td>1.4358860e+06</td><td>1.2779312e+02</td><td>4.0466931e+03</td><td>1.5422539e+01</td><td>1.4646795e+06</td><td>1.3039951e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64438</td><td>8.4074054e-05</td><td>260.73540</td><td>1.3953059e-04</td><td>5.5579260e-02</td><td>-1.1038263e-02</td></tr>
    <tr><td>1353.1659550506233</td><td>1.4649392e+06</td><td>1.3041254e+02</td><td>7.9325796e-04</td><td>90511</td><td>1630.64849</td><td>260.73625</td><td>1.4361424e+06</td><td>1.2780590e+02</td><td>4.0677520e+03</td><td>1.5430614e+01</td><td>1.4649392e+06</td><td>1.3041254e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64849</td><td>8.4072431e-05</td><td>260.73625</td><td>1.3956340e-04</td><td>6.0031198e-02</td><td>-1.2474478e-02</td></tr>
    <tr><td>1353.167343906477</td><td>1.4646214e+06</td><td>1.3039377e+02</td><td>7.9322548e-04</td><td>90512</td><td>1630.64657</td><td>260.73713</td><td>1.4357276e+06</td><td>1.2778750e+02</td><td>4.0519436e+03</td><td>1.5423266e+01</td><td>1.4646214e+06</td><td>1.3039377e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64657</td><td>8.4076637e-05</td><td>260.73713</td><td>1.3951116e-04</td><td>5.7689309e-02</td><td>-9.8480135e-03</td></tr>
    <tr><td>1353.1687327622717</td><td>1.4647834e+06</td><td>1.3040990e+02</td><td>7.9319294e-04</td><td>90513</td><td>1630.65187</td><td>260.73559</td><td>1.4359665e+06</td><td>1.2780331e+02</td><td>4.0945930e+03</td><td>1.5460280e+01</td><td>1.4647834e+06</td><td>1.3040990e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.65187</td><td>8.4072963e-05</td><td>260.73559</td><td>1.3958018e-04</td><td>6.3572161e-02</td><td>-1.4975319e-02</td></tr>
    <tr><td>1353.170121618124</td><td>1.4644656e+06</td><td>1.3038603e+02</td><td>7.9316046e-04</td><td>90514</td><td>1630.64304</td><td>260.71503</td><td>1.4355525e+06</td><td>1.2777991e+02</td><td>4.0659807e+03</td><td>1.5433553e+01</td><td>1.4644656e+06</td><td>1.3038603e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64304</td><td>8.4104897e-05</td><td>260.71503</td><td>1.3954782e-04</td><td>5.4697301e-02</td><td>-3.3739604e-02</td></tr>
    <tr><td>1353.1715104739196</td><td>1.4647081e+06</td><td>1.3039996e+02</td><td>7.9312793e-04</td><td>90515</td><td>1630.64598</td><td>260.73359</td><td>1.4358651e+06</td><td>1.2779357e+02</td><td>4.0584336e+03</td><td>1.5429242e+01</td><td>1.4647081e+06</td><td>1.3039996e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64598</td><td>8.4103733e-05</td><td>260.73359</td><td>1.3949537e-04</td><td>5.7749905e-02</td><td>-1.5640877e-02</td></tr>
    <tr><td>1353.1728993297734</td><td>1.4646606e+06</td><td>1.3040236e+02</td><td>7.9309545e-04</td><td>90516</td><td>1630.65524</td><td>260.73718</td><td>1.4357864e+06</td><td>1.2779591e+02</td><td>4.0737170e+03</td><td>1.5449224e+01</td><td>1.4646606e+06</td><td>1.3040236e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.65524</td><td>8.4154504e-05</td><td>260.73718</td><td>1.3958884e-04</td><td>6.7496188e-02</td><td>-1.1539744e-02</td></tr>
    <tr><td>1353.1742881855687</td><td>1.4648560e+06</td><td>1.3041582e+02</td><td>7.9306291e-04</td><td>90517</td><td>1630.65059</td><td>260.74847</td><td>1.4360880e+06</td><td>1.2780910e+02</td><td>4.0896948e+03</td><td>1.5452563e+01</td><td>1.4648560e+06</td><td>1.3041582e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.65059</td><td>8.4090752e-05</td><td>260.74847</td><td>1.3948027e-04</td><td>6.1896853e-02</td><td>3.0782772e-03</td></tr>
    <tr><td>1353.1756770414217</td><td>1.4646049e+06</td><td>1.3039998e+02</td><td>7.9303043e-04</td><td>90518</td><td>1630.64159</td><td>260.71763</td><td>1.4359089e+06</td><td>1.2779358e+02</td><td>4.0475869e+03</td><td>1.5419288e+01</td><td>1.4646049e+06</td><td>1.3039998e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.64159</td><td>8.4079904e-05</td><td>260.71763</td><td>1.3953699e-04</td><td>5.2571520e-02</td><td>-3.2142449e-02</td></tr>
    <tr><td>1353.1770658972157</td><td>1.4646141e+06</td><td>1.3040526e+02</td><td>7.9299789e-04</td><td>90519</td><td>1630.65089</td><td>260.74716</td><td>1.4358994e+06</td><td>1.2779876e+02</td><td>4.0689077e+03</td><td>1.5450690e+01</td><td>1.4646141e+06</td><td>1.3040526e+02</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>1630.65089</td><td>8.4083091e-05</td><td>260.74716</td><td>1.3951387e-04</td><td>6.2483948e-02</td><td>-7.1828649e-04</td></tr>
    </table>



In this table, you are given the time and the flux for your object of
interest. There does however seem to be three entries for flux: flux,
sap_flux, and pdcsap_flux. By default, the flux = pdcsap_flux, but what
do these entries mean?

-  **Simple Aperture Photometry (SAP)**: The SAP light curve is
   calculated by summing together the brightness of pixels that fall
   within an aperture set by the *TESS* mission. This is often referred
   to as the *optimal aperture*, but despite its name, it can sometimes
   be improved upon! Because the SAP light curve is a sum of the
   brightness in chosen pixels, it is still subject to systematic
   artifacts of the mission.

-  **Pre-search Data Conditioning SAP flux (PDCSAP) flux**: SAP flux
   from which long-term trends have been removed using so-called
   Co-trending Basis Vectors (CBVs). PDCSAP flux is usually cleaner data
   than the SAP flux and will have fewer systematic trends.

You can switch between fluxes using the following commands,

::

   pdcsap = lcf[0].pdcsap_flux

   sapflux = lcf[0].sap_flux

Let’s now plot both the PDCSAP and SAP light curves and see what they
look like.

.. code:: ipython3

    ax = lcf[0].plot(column='sap_flux', normalize=True, label="SAP");
    lcf[0].plot(ax=ax, column='pdcsap_flux', normalize=True, label="PDCSAP");



.. image::  images/HowToFindAnExoplanet-UserVersion/output_21_0.png
    :alt: TESS SPOC lightcurves


There are some big differences between these two light curves,
specifically the dips in the SAP light curve and its overall gradent.
These differences will be discussed later in the tutorial. For now,
let’s think about how we can manipulate the light curves.

1.2.1 Manipulating a light curve
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are a set of useful functions in *Lightkurve* which you can use to
work with the data. These include:

-  `flatten() <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.LightCurve.flatten.html?highlight=flatten#lightkurve.LightCurve.flatten>`__:
   Remove long term trends using a Savitzky–Golay filter
-  `remove_outliers() <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.LightCurve.remove_outliers.html?highlight=remove_outliers>`__:
   Remove outliers using simple sigma clipping
-  `remove_nans() <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.LightCurve.remove_nans.html?highlight=remove_nans>`__:
   Remove infinite or NaN values (these can occur during thruster
   firings)
-  `fold() <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.LightCurve.fold.html?highlight=fold>`__:
   Fold the data at a particular period
-  `bin() <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.LightCurve.bin.html?highlight=bin#lightkurve.LightCurve.bin>`__:
   Reduce the time resolution of the array, taking the average value in
   each bin.

We can use these simply on a light curve object. For this tutorial,
let’s stick with the PDCSAP flux.

.. code:: ipython3

    ax = lcf[0].plot() 
    ax.set_title("PDCSAP light curve of  Pi Mensae")




.. parsed-literal::

    Text(0.5, 1.0, 'PDCSAP light curve of  Pi Mensae')




.. image:: images/HowToFindAnExoplanet-UserVersion/output_23_1.png
    :alt: Pi Mensae lightcurve


We can kind of make out a possible transit but let us manipulate the
light curve some more to see if we can pull it out.

Flattening
~~~~~~~~~~

.. code:: ipython3

    flat_lc = lcf[0].flatten(window_length=1001)
    flat_lc.plot();



.. image:: images/HowToFindAnExoplanet-UserVersion/output_25_0.png
    :alt: Flattened lightcurve


The light curve looks much flatter. Unfortunately, there is a portion of
the light curve that is very noisy, due to a jitter in the TESS
spacecraft. We can remove this simply by masking the light curve. First,
we’ll select the times that had the jitter.

.. code:: ipython3

    # Flag the times that are good quality
    mask = (flat_lc.time.value < 1346) | (flat_lc.time.value > 1350)

.. code:: ipython3

    masked_lc = flat_lc[mask]
    masked_lc.plot()




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb070571ed0>




.. image:: images/HowToFindAnExoplanet-UserVersion/output_28_1.png
    :alt: Flattened lightcurve with mask


We can use Lightkurve to plot these two light curves over each other to
see the difference.

.. code:: ipython3

    # First define the `matplotlib.pyplot.axes`
    ax = flat_lc.plot()
    
    # Pass that axis to the next plot
    masked_lc.plot(ax=ax, label='masked');



.. image:: images/HowToFindAnExoplanet-UserVersion/output_30_0.png
    :alt: Flattened lightcurve mask comparison


This looks much better. Now we might want to clip out some outliers from
the light curve. We can do that with a simple *Lightkurve* function
remove_outliers().

Remove outliers
~~~~~~~~~~~~~~~

.. code:: ipython3

    clipped_lc = masked_lc.remove_outliers(sigma=6)
    clipped_lc.plot();



.. image:: images/HowToFindAnExoplanet-UserVersion/output_33_0.png
    :alt: Lightcurve with outliers removed


Finally, let’s use *Lightkurve* to fold the data at the exoplanet
orbital period and see if we can detect the transit.

Folding the light curve and finding the transit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the Pi Mensae paper, we know that planet c has a period of 6.27
days. We can use the ``fold()`` function to find the transit in our data
as shown below.

.. code:: ipython3

    folded_lc = clipped_lc.fold(period=6.27, epoch_time=1325.504)
    folded_lc.plot();



.. image:: images/HowToFindAnExoplanet-UserVersion/output_36_0.png
    :alt: Lightcurve folded on transit


It looks like there’s something there, but it’s hard to see. Let’s bin
the light curve to reduce the number of points, but also reduce the
uncertainty of those points.

Binning the light curve
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    import astropy.units as u
    binned_lc = folded_lc.bin(time_bin_size=5*u.minute)
    binned_lc.errorbar();



.. image:: images/HowToFindAnExoplanet-UserVersion/output_38_0.png
    :alt: Binned lightcurve folded on transit


And now we can see the transit of Pi Mensae c!

2. Creating a light curve using FFI data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In our previous FFI search, we found that *Pi Men* was observed in
Sector 1 with a 30-min cadence. This data is stored as the 1st argument
of the *search_ffi* array.

To create the light curve from the FFI data, we must first download the
relevant images. Note that we do not want the entirety of the Sector 1
FFI, only a small region surrounding our object of interest. We can
specify the size of the region we want to cut out using the commands
below, in this case we want a 10x10 pixel region.

.. code:: ipython3

    ffi_data = search_ffi[0].download(cutout_size=10)

Let’s now see what this cut out looks like and also check that our
object is at the center of it.

.. code:: ipython3

    ffi_data.plot()




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb0945b2190>




.. image:: images/HowToFindAnExoplanet-UserVersion/output_43_1.png
    :alt: Target Pixel File of Pi Mensae


The above figure indicates the pixels on the CCD camera, with which *Pi
Men* was observed. The color indicates the amount of flux in each pixel,
in electrons per second. The y-axis shows the pixel row, and the x-axis
shows the pixel column. The title tells us the *TESS* Input Catalogue
(`TIC <https://tess.mit.edu/science/tess-input-catalogue/>`__)
identification number of the target, and the observing cadence of this
image. By default, ``plot()`` shows the first observation cadence in the
Sector.

It looks like our star is isolated, so we can extract a light-curve by
simply summing up all the pixel values in each image. To do this, we
need to first define an **aperture mask**.

Many decisions go into the choice of aperture mask, including the
significant blending of the large *TESS* pixels. In this tutorial, we
are going to define an aperture by defining a median flux value and only
selecting pixels at a certain sigma above that threshold.

In most situations, a threshold mask will be the best choice for custom
aperture photometry, as it doesn’t involve trial and error beyond
finding the best sigma value. You can define a threshold mask using the
following code:

.. code:: ipython3

    target_mask = ffi_data.create_threshold_mask(threshold=10, reference_pixel='center')
    n_target_pixels = target_mask.sum()
    n_target_pixels




.. parsed-literal::

    18



This indicates that there are 18 pixels which are above our threshold
and so in our mask. We can now check to make sure that our target is
covered by this mask using plot.

.. code:: ipython3

    ffi_data.plot(aperture_mask=target_mask, mask_color='r')




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb0d19c3e90>




.. image:: images/HowToFindAnExoplanet-UserVersion/output_47_1.png
    :alt: Target Pixel File with Pi Mensae target aperture


Nice! We see our target mask centered on the 18 brightest pixels in the
center of the image. Let’s see what the light curve looks like. Note
that this light curve will be uncorrected for any anomalies or noise,
and that the flux is therefore based upon “Simple Aperture Photometry”
(SAP).

To create our light curve, we will pass our **aperture_mask** to the
```to_lightcurve`` <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.KeplerTargetPixelFile.to_lightcurve.html?highlight=to_lightcurve>`__
function.

.. code:: ipython3

    ffi_lc = ffi_data.to_lightcurve(aperture_mask=target_mask)

Once again, we can examine the light curve data as a table, but note
this time that there is only one flux value and that as default, this is
the SAP flux.

.. code:: ipython3

    ffi_lc




.. raw:: html

    <i>TessLightCurve length=1267 LABEL=&quot;&quot; SECTOR=1</i>
    <table id="table140396326850448" class="table-striped table-bordered table-condensed">
    <thead><tr><th>time</th><th>flux</th><th>flux_err</th><th>centroid_col</th><th>centroid_row</th><th>cadenceno</th><th>quality</th></tr></thead>
    <thead><tr><th></th><th>electron / s</th><th>electron / s</th><th>pix</th><th>pix</th><th></th><th></th></tr></thead>
    <thead><tr><th>object</th><th>float32</th><th>float32</th><th>float64</th><th>float64</th><th>int64</th><th>int32</th></tr></thead>
    <tr><td>1325.324261183436</td><td>1316430.75</td><td>31.303890228271484</td><td>1630.6385441885782</td><td>260.61400004745315</td><td>0</td><td>0</td></tr>
    <tr><td>1325.345094309689</td><td>1316496.0</td><td>31.304616928100586</td><td>1630.63890532941</td><td>260.614058268241</td><td>1</td><td>0</td></tr>
    <tr><td>1325.3659274373958</td><td>1316588.125</td><td>31.30562400817871</td><td>1630.6395243879658</td><td>260.61363650321783</td><td>2</td><td>0</td></tr>
    <tr><td>1325.386760566499</td><td>1316589.0</td><td>31.305648803710938</td><td>1630.6392641770467</td><td>260.61324889099075</td><td>3</td><td>0</td></tr>
    <tr><td>1325.407593697</td><td>1316634.125</td><td>31.306297302246094</td><td>1630.6403961686917</td><td>260.61333124245886</td><td>4</td><td>0</td></tr>
    <tr><td>1325.4284268288402</td><td>1316664.875</td><td>31.306610107421875</td><td>1630.6403907997208</td><td>260.61168543184255</td><td>5</td><td>0</td></tr>
    <tr><td>1325.4492599619616</td><td>1316503.25</td><td>31.304628372192383</td><td>1630.6404545748724</td><td>260.6105785492981</td><td>6</td><td>0</td></tr>
    <tr><td>1325.470093096421</td><td>1316347.125</td><td>31.30280113220215</td><td>1630.6417255479462</td><td>260.61074264747987</td><td>7</td><td>0</td></tr>
    <tr><td>1325.490926232102</td><td>1316419.875</td><td>31.303749084472656</td><td>1630.6415727513183</td><td>260.61034411311493</td><td>8</td><td>0</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>1352.969791263754</td><td>1315211.75</td><td>31.292274475097656</td><td>1630.6482825671299</td><td>260.73213581832687</td><td>1257</td><td>0</td></tr>
    <tr><td>1352.9906242420939</td><td>1315086.25</td><td>31.29055404663086</td><td>1630.6484335940063</td><td>260.73307489515895</td><td>1258</td><td>0</td></tr>
    <tr><td>1353.011457219852</td><td>1315193.75</td><td>31.29180908203125</td><td>1630.646707975239</td><td>260.731500817073</td><td>1259</td><td>0</td></tr>
    <tr><td>1353.0322901970571</td><td>1315158.75</td><td>31.291419982910156</td><td>1630.648037172556</td><td>260.73591222382134</td><td>1260</td><td>0</td></tr>
    <tr><td>1353.0531231737955</td><td>1315296.5</td><td>31.293004989624023</td><td>1630.647094118251</td><td>260.7333206378633</td><td>1261</td><td>0</td></tr>
    <tr><td>1353.0739561500686</td><td>1315088.125</td><td>31.290395736694336</td><td>1630.6473270669005</td><td>260.7351593432308</td><td>1262</td><td>0</td></tr>
    <tr><td>1353.0947891259361</td><td>1315222.125</td><td>31.29218864440918</td><td>1630.6474165571676</td><td>260.7348915744579</td><td>1263</td><td>0</td></tr>
    <tr><td>1353.1156221014514</td><td>1315163.875</td><td>31.29137420654297</td><td>1630.6464359975553</td><td>260.7340468639079</td><td>1264</td><td>0</td></tr>
    <tr><td>1353.136455076648</td><td>1315184.125</td><td>31.291683197021484</td><td>1630.6479758585133</td><td>260.7343014005144</td><td>1265</td><td>0</td></tr>
    <tr><td>1353.1572880516123</td><td>1315330.875</td><td>31.293392181396484</td><td>1630.6465981702963</td><td>260.73701035906174</td><td>1266</td><td>0</td></tr>
    </table>



Let’s now plot this,

.. code:: ipython3

    ffi_lc.scatter(label="SAP FFI")




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb0d1babc50>




.. image:: images/HowToFindAnExoplanet-UserVersion/output_53_1.png
    :alt: Pi Mensae raw lightcurve


We can see that there are problematic data points in this light curve
which are probably due to jitter. Once again, we can remove these data
points via creating and applying a mask.

.. code:: ipython3

    mask_ffi = (ffi_lc.time.value < 1346) | (ffi_lc.time.value > 1350)
    masked_lc_ffi = ffi_lc[mask_ffi]
    masked_lc_ffi.plot()




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb0d1bab050>




.. image:: images/HowToFindAnExoplanet-UserVersion/output_55_1.png
    :alt: Pi Mensae lightcurve with removed bad data


OK, this looks a bit better but we should also clip the data again.

.. code:: ipython3

    clipped_ffi = masked_lc_ffi.remove_outliers(sigma=6)
    clipped_ffi.plot();



.. image:: images/HowToFindAnExoplanet-UserVersion/output_57_0.png
    :alt: Pi Mensae lightcurve with outliers removed


Looking at the above light curve, we can see that there are still a few
odd trends that need to be addressed, but there is also strong evidence
for the previously observed transit! We can try to clean up our data a
little using *Lightkurve’s* built in corrector class functions. These
functions are very useful for removing scattered light and other
effects. You can learn more about them
`here <https://lightkurve.github.io/lightkurve/tutorials/index.html#removing-instrumental-noise>`__.

In this example, we are going to use the Pixel Level Decorrelation (PLD)
Corrector (PLDCorrect). The PLD method has primarily been used to remove
systematic trends introduced by small spacecraft motions during
observations and has been shown to be successful at improving the
precision of data taken by the Spitzer space telescope. PLD works by
identifying a set of trends in the pixels surrounding the target star
and performing linear regression to create a combination of these trends
that effectively models the systematic noise introduced by spacecraft
motion. This noise model is then subtracted from the uncorrected light
curve. We can apply it to our data using the code shown below.

.. code:: ipython3

    from lightkurve.correctors import PLDCorrector
    pld = PLDCorrector(ffi_data[mask_ffi], aperture_mask=target_mask)
    pld.correct(pca_components=3)
    pltAxis = pld.diagnose()
    
    corrected_ffi = pld.correct(pca_components=3)



.. image:: images/HowToFindAnExoplanet-UserVersion/output_59_0.png
    :alt: Pi Mensae lightcurve with PLD correction


The above plots indicate the corrections applied to our light curve. It
removed a background and applied a spline; outliers are also presented.
Let’s now plot up our corrected light curve and compare to the corrected
flux to the non-corrected flux.

.. code:: ipython3

    ax = ffi_lc.plot(normalize=True, label="SAP FFI");
    corrected_ffi.remove_outliers().plot(ax=ax,normalize=True,label="SAP FFI corrected")
    plt.ylim(0.9975,1.0025)




.. parsed-literal::

    (0.9975, 1.0025)




.. image:: images/HowToFindAnExoplanet-UserVersion/output_61_1.png
    :alt: Pi Mensae lightcurve comparison


We can see that the corrector removed a lot of the trends that we were
seeing. Let’s now proceed as we did before and compare the results.
First we need to ``flatten()``.

.. code:: ipython3

    ffi_flat_lc = corrected_ffi.flatten(window_length=1001)
    ffi_flat_lc.plot()




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb09473f4d0>




.. image:: images/HowToFindAnExoplanet-UserVersion/output_63_1.png
    :alt: Pi Mensae flattened lightcurve


Now we need to ``fold()``.

.. code:: ipython3

    folded_ffi = ffi_flat_lc.fold(period=6.27, epoch_time=1325.504)
    folded_ffi.plot()
    plt.ylim(0.999,1.001)




.. parsed-literal::

    (0.999, 1.001)




.. image:: images/HowToFindAnExoplanet-UserVersion/output_65_1.png
    :alt: Pi Mensae folded lightcurve


It is a little noiser than before and a bit more difficult to see due to
the longer cadence (30-min), but we can clearly make out the transit
again. Let’s compare this to our earlier light curve.

.. code:: ipython3

    ax = folded_lc.plot(label="LightCurve Object")
    folded_ffi.plot(ax=ax, label="FFI")




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb0a1d59890>




.. image:: images/HowToFindAnExoplanet-UserVersion/output_67_1.png
    :alt: Pi Mensae FFI lightcurve comparison


Great! The transit is shown in both cases. It is clear more work needs
to be done on the FFI to remove noise and instrumental trends from the
data, but this is a good start!

Additional Resources
--------------------

In this tutorial, we have covered the basics of how to obtain, reduce
and analyze *TESS* data using *Lightkurve*. We have, however, only
skimmed the surface of what *Lightkurve* can do and how to investigate
the data. For more detailed tutorials as well as other useful tools,
please visit the following pages.

-  `Lightkurve Tutorials
   page <https://lightkurve.github.io/lightkurve/tutorials/index.html#>`__: A set of
   21 tutorials dealing with Kepler/K2 and TESS data
-  `TESS GI data products
   page <https://heasarc.gsfc.nasa.gov/docs/tess/data-analysis-tools.html>`__:
   A set of 7 TESS specific tutorials.
-  `STScI Kepler K3
   notebooks <https://github.com/spacetelescope/notebooks/tree/master/notebooks/MAST/Kepler>`__:
   A set of notebooks produced by a collaboration between NumFocus,
   MAST, *Lightkurve*, and TESS GI office. They make use of python
   astronomical data packages to demonstrate how to analyze time series
   data from these NASA missions. New tools are presented here and also
   techniques for the advanced user.

Authors
-------

`Rebekah
Hounsell <https://heasarc.gsfc.nasa.gov/docs/tess/helpdesk.html>`__
(with help from the Lightkurve Collaboration, 2018) - Support scientist
for *TESS* in the NASA GSFC GI Office. For more help with TESS data,
please contact us at tesshelp@bigbang.gsfc.nasa.gov.
