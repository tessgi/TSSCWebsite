TSC2 Intro
##########
:save_as: TSC2-Intro.html
	  
An introduction into the tools and tutorials available for the analysis of TESS data
====================================================================================

Welcome everyone to our *TESS* Lightkurve splinter session!

Authors
-------

`Rebekah
Hounsell <https://heasarc.gsfc.nasa.gov/docs/tess/helpdesk.html>`__ -
Support scientist for *TESS* in the NASA GSFC GI Office.

.. image:: images/helpdesk.png
    :alt: Helpdesk Personnel

Download the notebook
=====================

If you would like to download a copy of this notebook you can do so by clicking the link below

.. raw:: html

   <p><a class="reference download internal" href="https://tessgi.github.io/TessGiWebsite/docs/tutorials/TSC2-Intro.ipynb">
   <tt class="xref download docutils literal">
   DOWNLOAD
   </tt></a><p>


Learning Goals
--------------

In this tutorial, we will teach the user how to access, analyze, and
manipulate data from the NASA Exoplanet mission *TESS* (this can also be
applied to *Kepler* & *K2*). All tools presented will teach the user how
to work with time series data for the purpose of scientific research.

The workshop assumes a basic knowledge of python and astronomy, and will
walk the user through several of the concepts outlined below:

1. How to obtain *TESS* data products from the MAST archive
2. How to use *Lightkurve* to access the various data products and
   create time series
3. How to analyze and assess various data anomalies and how you might
   visualize them

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

If you are not that experienced with *Python*, or cannot download
*Lightkurve*, you can run this notebook as a `Colab
notebook <https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index>`__.
Colaboratory allows users to write and execute *Python* in your browser
with zero configuration required.

All you need is a Google account and to copy and paste in the following
command at the top of your colab notebook:

``!pip install lightkurve``

This downloads the *Lightkurve* package.

Introduction to *TESS*:
-----------------------

The *Transiting Exoplanet Survey Satellite (TESS)* is a NASA-sponsored
Astrophysics Explorer-class mission that is performing a near all-sky
survey to search for planets transiting nearby stars. *TESS* completed
its primary mission in July of 2020, and has now entered its extended
mission. The current extended mission will last until September 2022,
and will continue to scan the sky for exoplanets and transient events.
The *TESS* mission is now more community focused with a larger guest
investigator (GI) program.

Over the last three years *TESS* has observed both the northern and
southern hemispheres, with each hemisphere being split into ~13 sectors.
Each sector is observed for ~27 days by *TESS’s* four cameras.

.. image:: images/sector.png
    :alt: TESS sector observing strategy

The main data products collected by the *TESS* mission are described
below.

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

1. How to obtain *TESS* data products from the MAST archive
-----------------------------------------------------------

You can access *TESS*, *Kepler*, and *K2* data via the `Mikulksi Archive
for Space Telescopes
(MAST) <https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html>`__
archive or via the *Lightkurve* package (see Section 2).

Here, we are focusing on obtaining your data via the MAST portal.
Using the portal, you can enter the name of your object, its TIC number, or
position (i.e., R.A and Dec). If listed in the archive, the table
containing each observation will be returned.

.. raw:: html

   <video width="100%" height="100%" controls src="MAST-recording.mov" />

2. How to use *Lightkurve* to access the various data products and create a time series
---------------------------------------------------------------------------------------

`Lightkurve <https://lightkurve.github.io/lightkurve/index.html>`__ offers
a user-friendly way to analyze time series data obtained by telescopes,
in particular *NASA’s Kepler* and *TESS* exoplanet missions. You can
search for the various data products for *TESS* on MAST using the
following *Lightkurve* functions:

-  To look for your object in a full frame image:
   ```search_tesscut()`` <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.search_tesscut.html?highlight=search_tesscut>`__

-  To look for target pixel files:
   ```search_targetpixelfile()`` <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.search_targetpixelfile.html?highlight=search_targetpixelfile>`__

-  To obtain light curve files for your object of interest:
   ```search_lightcurve()`` <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.search_lightcurve.html?highlight=search_lightcurve>`__

For the purpose of this tutorial, we will be examining `L
98-59 <https://arxiv.org/pdf/1903.08017.pdf>`__, a bright M dwarf star
at a distance of 10.6 pc. This star is host to three terrestrial-sized
planets and is also known in the *TESS* system as TIC 307210830.

2.1 Accessing the data products
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let’s go through each one of the above functions and see what data is
available.

.. code:: ipython3

    search_ffi = lk.search_tesscut('L 98-59')
    search_tpf = lk.search_targetpixelfile('L 98-59')
    search_lcf = lk.search_lightcurve('L 98-59')

.. code:: ipython3

    search_ffi




.. raw:: html

    SearchResult containing 15 data products.
    
    <table id="table140208156282192">
    <thead><tr><th>#</th><th>mission</th><th>year</th><th>author</th><th>exptime</th><th>target_name</th><th>distance</th></tr></thead>
    <thead><tr><th></th><th></th><th></th><th></th><th>s</th><th></th><th>arcsec</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 01</td><td>2018</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 02</td><td>2018</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 05</td><td>2018</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 09</td><td>2019</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 10</td><td>2019</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 11</td><td>2019</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>7</td><td>TESS Sector 12</td><td>2019</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>1426</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>8</td><td>TESS Sector 28</td><td>2020</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>9</td><td>TESS Sector 29</td><td>2020</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>10</td><td>TESS Sector 32</td><td>2020</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>11</td><td>TESS Sector 35</td><td>2021</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>12</td><td>TESS Sector 36</td><td>2021</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>13</td><td>TESS Sector 37</td><td>2021</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>L 98-59</td><td>0.0</td></tr>
    <tr><td>14</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://mast.stsci.edu/tesscut/'>TESScut</a></td><td>475</td><td>L 98-59</td><td>0.0</td></tr>
    </table>



The above table provides several important pieces of information: - The
sector in which the object was observed. - The year in which the object
was observed. - The author of the data. This has multiple options and
each is a hyperlink that when clicked will provide you with more
information. - The cadence of the observation. - The name of the target.
- The distance of the observation from your target of interest. This is
useful if you conduct a cone search around your objects co-ordinates.

The table above indicates that our object was observed in multiple
sectors. Note that in years 1 and 2 (2018 & 2019) that the cadence of
the FFI data was 30-min, but in year 3 (2020/2021) it is 10-min.

Let’s see if any other data exists - i.e., was it observed as a target
of interest and does it have a Target Pixel File.

.. code:: ipython3

    search_tpf




.. raw:: html

    SearchResult containing 28 data products.
    
    <table id="table140208682983824">
    <thead><tr><th>#</th><th>mission</th><th>year</th><th>author</th><th>exptime</th><th>target_name</th><th>distance</th></tr></thead>
    <thead><tr><th></th><th></th><th></th><th></th><th>s</th><th></th><th>arcsec</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 02</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 02</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 05</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 05</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 09</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 10</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>7</td><td>TESS Sector 11</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>8</td><td>TESS Sector 12</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>9</td><td>TESS Sector 28</td><td>2020</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>18</td><td>TESS Sector 35</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>19</td><td>TESS Sector 35</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>20</td><td>TESS Sector 36</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>21</td><td>TESS Sector 36</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>22</td><td>TESS Sector 37</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>23</td><td>TESS Sector 37</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>24</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>25</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>26</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>27</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    </table>
    Length = 28 rows



Great! Our object was observed as a target of interest and has 2-min and
20-sec cadenced data. This means that there should be light curve files
already on the archive. Let’s check those out.

.. code:: ipython3

    search_lcf




.. raw:: html

    SearchResult containing 38 data products.
    
    <table id="table140208156281744">
    <thead><tr><th>#</th><th>mission</th><th>year</th><th>author</th><th>exptime</th><th>target_name</th><th>distance</th></tr></thead>
    <thead><tr><th></th><th></th><th></th><th></th><th>s</th><th></th><th>arcsec</th></tr></thead>
    <tr><td>0</td><td>TESS Sector</td><td>2018</td><td>DIAMANTE</td><td>1800</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 02</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 02</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 02</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/qlp'>QLP</a></td><td>1800</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 02</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tasoc'>TASOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 02</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tasoc'>TASOC</a></td><td>1800</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 05</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>7</td><td>TESS Sector 05</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/tess-spoc'>TESS-SPOC</a></td><td>1800</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>8</td><td>TESS Sector 05</td><td>2018</td><td><a href='https://archive.stsci.edu/hlsp/qlp'>QLP</a></td><td>1800</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>9</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>28</td><td>TESS Sector 35</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>29</td><td>TESS Sector 35</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>30</td><td>TESS Sector 36</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>31</td><td>TESS Sector 36</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>32</td><td>TESS Sector 37</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>33</td><td>TESS Sector 37</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>34</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>35</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>36</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>20</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>37</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    </table>
    Length = 38 rows



Wonderful! Light curves for our object of interest have already been
created.

2.2 Creating a light curve using a Light Curve File:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now on to getting the light curve for our object of interest. From the
above table, it looks like there are multiple authors for our target.
For the purpose of this tutorial, let’s stick to “SPOC” data products
which have a 2-min cadence. We can return only these results using the
following commands.

.. code:: ipython3

    search_lcf_refined = lk.search_lightcurve('L 98-59', author="SPOC", exptime=120)
    search_lcf_refined 




.. raw:: html

    SearchResult containing 15 data products.
    
    <table id="table140208683094800">
    <thead><tr><th>#</th><th>mission</th><th>year</th><th>author</th><th>exptime</th><th>target_name</th><th>distance</th></tr></thead>
    <thead><tr><th></th><th></th><th></th><th></th><th>s</th><th></th><th>arcsec</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 02</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 05</td><td>2018</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 08</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 09</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 10</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 11</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 12</td><td>2019</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>7</td><td>TESS Sector 28</td><td>2020</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>8</td><td>TESS Sector 29</td><td>2020</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>9</td><td>TESS Sector 32</td><td>2020</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>10</td><td>TESS Sector 35</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>11</td><td>TESS Sector 36</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>12</td><td>TESS Sector 37</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>13</td><td>TESS Sector 38</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    <tr><td>14</td><td>TESS Sector 39</td><td>2021</td><td><a href='https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html'>SPOC</a></td><td>120</td><td>307210830</td><td>0.0</td></tr>
    </table>



We now see five search results. Let’s download these and see what the
light curve looks like.

.. code:: ipython3

    lcf = search_lcf_refined.download_all()

.. code:: ipython3

    lcf




.. parsed-literal::

    LightCurveCollection of 15 objects:
        0: <TessLightCurve LABEL="TIC 307210830" SECTOR=2 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        1: <TessLightCurve LABEL="TIC 307210830" SECTOR=5 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        2: <TessLightCurve LABEL="TIC 307210830" SECTOR=8 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        3: <TessLightCurve LABEL="TIC 307210830" SECTOR=9 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        4: <TessLightCurve LABEL="TIC 307210830" SECTOR=10 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        5: <TessLightCurve LABEL="TIC 307210830" SECTOR=11 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        6: <TessLightCurve LABEL="TIC 307210830" SECTOR=12 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        7: <TessLightCurve LABEL="TIC 307210830" SECTOR=28 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        8: <TessLightCurve LABEL="TIC 307210830" SECTOR=29 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        9: <TessLightCurve LABEL="TIC 307210830" SECTOR=32 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        10: <TessLightCurve LABEL="TIC 307210830" SECTOR=35 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        11: <TessLightCurve LABEL="TIC 307210830" SECTOR=36 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        12: <TessLightCurve LABEL="TIC 307210830" SECTOR=37 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        13: <TessLightCurve LABEL="TIC 307210830" SECTOR=38 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>
        14: <TessLightCurve LABEL="TIC 307210830" SECTOR=39 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux>



This has downloaded the light curve for each sector, and stored the data
in arrays. You can look at the data for a specific sector by specifying
an array number as indicated below. This displays the data for sector 2
as a table.

.. code:: ipython3

    lcf[0]




.. raw:: html

    <i>TessLightCurve length=18300 LABEL=&quot;TIC 307210830&quot; SECTOR=2 AUTHOR=SPOC FLUX_ORIGIN=pdcsap_flux</i>
    <table id="table140208421568400" class="table-striped table-bordered table-condensed">
    <thead><tr><th>time</th><th>flux</th><th>flux_err</th><th>timecorr</th><th>cadenceno</th><th>centroid_col</th><th>centroid_row</th><th>sap_flux</th><th>sap_flux_err</th><th>sap_bkg</th><th>sap_bkg_err</th><th>pdcsap_flux</th><th>pdcsap_flux_err</th><th>quality</th><th>psf_centr1</th><th>psf_centr1_err</th><th>psf_centr2</th><th>psf_centr2_err</th><th>mom_centr1</th><th>mom_centr1_err</th><th>mom_centr2</th><th>mom_centr2_err</th><th>pos_corr1</th><th>pos_corr2</th></tr></thead>
    <thead><tr><th></th><th>electron / s</th><th>electron / s</th><th>d</th><th></th><th>pix</th><th>pix</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th>electron / s</th><th></th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th><th>pix</th></tr></thead>
    <thead><tr><th>object</th><th>float32</th><th>float32</th><th>float32</th><th>int32</th><th>float64</th><th>float64</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>int32</th><th>float64</th><th>float32</th><th>float64</th><th>float32</th><th>float64</th><th>float32</th><th>float64</th><th>float32</th><th>float32</th><th>float32</th></tr></thead>
    <tr><td>1354.1074113410245</td><td>2.4635420e+04</td><td>1.8856627e+01</td><td>-8.0586493e-04</td><td>91190</td><td>664.04462</td><td>338.97644</td><td>2.3127123e+04</td><td>1.7658133e+01</td><td>1.8465968e+03</td><td>5.2003989e+00</td><td>2.4635420e+04</td><td>1.8856627e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.04462</td><td>6.2346959e-04</td><td>338.97644</td><td>6.9568102e-04</td><td>3.1294446e-02</td><td>1.5483069e-01</td></tr>
    <tr><td>1354.1088002024744</td><td>2.4656008e+04</td><td>1.8861403e+01</td><td>-8.0589182e-04</td><td>91191</td><td>664.05609</td><td>338.96900</td><td>2.3150639e+04</td><td>1.7662607e+01</td><td>1.8428802e+03</td><td>5.1911125e+00</td><td>2.4656008e+04</td><td>1.8861403e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.05609</td><td>6.2315754e-04</td><td>338.96900</td><td>6.9629494e-04</td><td>4.3172963e-02</td><td>1.4587776e-01</td></tr>
    <tr><td>1354.110189063866</td><td>2.4635619e+04</td><td>1.8864876e+01</td><td>-8.0591877e-04</td><td>91192</td><td>664.07351</td><td>338.95814</td><td>2.3137189e+04</td><td>1.7665859e+01</td><td>1.8525369e+03</td><td>5.2004828e+00</td><td>2.4635619e+04</td><td>1.8864876e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07351</td><td>6.2400498e-04</td><td>338.95814</td><td>6.9669099e-04</td><td>6.0803384e-02</td><td>1.3428329e-01</td></tr>
    <tr><td>1354.1129667867635</td><td>2.4621027e+04</td><td>1.8853863e+01</td><td>-8.0597255e-04</td><td>91194</td><td>664.05132</td><td>338.94885</td><td>2.3098303e+04</td><td>1.7655546e+01</td><td>1.8542960e+03</td><td>5.2071209e+00</td><td>2.4621027e+04</td><td>1.8853863e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.05132</td><td>6.2639196e-04</td><td>338.94885</td><td>6.9927127e-04</td><td>3.7734102e-02</td><td>1.2694269e-01</td></tr>
    <tr><td>1354.1143556482134</td><td>2.4617400e+04</td><td>1.8859161e+01</td><td>-8.0599944e-04</td><td>91195</td><td>664.09017</td><td>338.97538</td><td>2.3127893e+04</td><td>1.7660507e+01</td><td>1.8433275e+03</td><td>5.1999226e+00</td><td>2.4617400e+04</td><td>1.8859161e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.09017</td><td>6.2417402e-04</td><td>338.97538</td><td>6.9604575e-04</td><td>7.8965843e-02</td><td>1.5301819e-01</td></tr>
    <tr><td>1354.1157445097215</td><td>2.4630531e+04</td><td>1.8860582e+01</td><td>-8.0602628e-04</td><td>91196</td><td>664.08357</td><td>338.96449</td><td>2.3136076e+04</td><td>1.7661839e+01</td><td>1.8441443e+03</td><td>5.1992383e+00</td><td>2.4630531e+04</td><td>1.8860582e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.08357</td><td>6.2411965e-04</td><td>338.96449</td><td>6.9649977e-04</td><td>7.2042428e-02</td><td>1.4030553e-01</td></tr>
    <tr><td>1354.117133371171</td><td>2.4625502e+04</td><td>1.8855038e+01</td><td>-8.0605317e-04</td><td>91197</td><td>664.08138</td><td>338.96244</td><td>2.3130492e+04</td><td>1.7656647e+01</td><td>1.8393002e+03</td><td>5.1891294e+00</td><td>2.4625502e+04</td><td>1.8855038e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.08138</td><td>6.2480610e-04</td><td>338.96244</td><td>6.9642899e-04</td><td>6.8586096e-02</td><td>1.3917884e-01</td></tr>
    <tr><td>1354.118522232678</td><td>2.4619252e+04</td><td>1.8856379e+01</td><td>-8.0608000e-04</td><td>91198</td><td>664.07300</td><td>338.95776</td><td>2.3123014e+04</td><td>1.7657902e+01</td><td>1.8428878e+03</td><td>5.1969514e+00</td><td>2.4619252e+04</td><td>1.8856379e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07300</td><td>6.2365801e-04</td><td>338.95776</td><td>6.9719343e-04</td><td>6.0448773e-02</td><td>1.3230386e-01</td></tr>
    <tr><td>1354.1199110941275</td><td>2.4591127e+04</td><td>1.8846928e+01</td><td>-8.0610689e-04</td><td>91199</td><td>664.07806</td><td>338.96029</td><td>2.3098383e+04</td><td>1.7649052e+01</td><td>1.8459741e+03</td><td>5.1905088e+00</td><td>2.4591127e+04</td><td>1.8846928e+01</td><td>0</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.07806</td><td>6.2481815e-04</td><td>338.96029</td><td>6.9739192e-04</td><td>6.4667158e-02</td><td>1.3584568e-01</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>1381.5000762208806</td><td>nan</td><td>nan</td><td>-1.1857160e-03</td><td>110913</td><td>664.02023</td><td>338.82238</td><td>2.3102398e+04</td><td>1.8364481e+01</td><td>3.0264915e+03</td><td>6.2652044e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.02023</td><td>6.5423414e-04</td><td>338.82238</td><td>7.4187893e-04</td><td>5.3329854e-03</td><td>-1.7557999e-02</td></tr>
    <tr><td>1381.5014650890794</td><td>nan</td><td>nan</td><td>-1.1857362e-03</td><td>110914</td><td>664.02570</td><td>338.81828</td><td>2.3131156e+04</td><td>1.8370392e+01</td><td>3.0202869e+03</td><td>6.2575917e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.02570</td><td>6.5429986e-04</td><td>338.81828</td><td>7.4093667e-04</td><td>1.0951885e-02</td><td>-1.8822383e-02</td></tr>
    <tr><td>1381.5028539571613</td><td>nan</td><td>nan</td><td>-1.1857564e-03</td><td>110915</td><td>664.02563</td><td>338.82131</td><td>2.3093904e+04</td><td>1.8351555e+01</td><td>3.0234182e+03</td><td>6.2496614e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.02563</td><td>6.5500144e-04</td><td>338.82131</td><td>7.4103329e-04</td><td>9.7870119e-03</td><td>-1.7654052e-02</td></tr>
    <tr><td>1381.50424282536</td><td>nan</td><td>nan</td><td>-1.1857765e-03</td><td>110916</td><td>664.01844</td><td>338.82636</td><td>2.3070465e+04</td><td>1.8338472e+01</td><td>3.0037410e+03</td><td>6.2505035e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.01844</td><td>6.5486954e-04</td><td>338.82636</td><td>7.4021460e-04</td><td>2.8580690e-03</td><td>-1.0282305e-02</td></tr>
    <tr><td>1381.5056316934429</td><td>nan</td><td>nan</td><td>-1.1857968e-03</td><td>110917</td><td>664.02351</td><td>338.81538</td><td>2.3084883e+04</td><td>1.8339640e+01</td><td>3.0044412e+03</td><td>6.2367158e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.02351</td><td>6.5468432e-04</td><td>338.81538</td><td>7.4014551e-04</td><td>8.9326696e-03</td><td>-2.2021463e-02</td></tr>
    <tr><td>1381.507020561642</td><td>nan</td><td>nan</td><td>-1.1858169e-03</td><td>110918</td><td>664.02287</td><td>338.81223</td><td>2.3056941e+04</td><td>1.8327822e+01</td><td>3.0007908e+03</td><td>6.2351022e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.02287</td><td>6.5470359e-04</td><td>338.81223</td><td>7.4105512e-04</td><td>7.0573296e-03</td><td>-2.6359776e-02</td></tr>
    <tr><td>1381.5084094298413</td><td>nan</td><td>nan</td><td>-1.1858371e-03</td><td>110919</td><td>664.02458</td><td>338.81035</td><td>2.3082803e+04</td><td>1.8332623e+01</td><td>2.9834062e+03</td><td>6.2297935e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.02458</td><td>6.5470277e-04</td><td>338.81035</td><td>7.4060517e-04</td><td>9.5733264e-03</td><td>-2.9673917e-02</td></tr>
    <tr><td>1381.5097982979241</td><td>nan</td><td>nan</td><td>-1.1858573e-03</td><td>110920</td><td>664.01752</td><td>338.82169</td><td>2.3091609e+04</td><td>1.8332087e+01</td><td>2.9773435e+03</td><td>6.2250428e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.01752</td><td>6.5375940e-04</td><td>338.82169</td><td>7.3996367e-04</td><td>3.0533469e-03</td><td>-1.5633952e-02</td></tr>
    <tr><td>1381.5111871661225</td><td>nan</td><td>nan</td><td>-1.1858775e-03</td><td>110921</td><td>664.02862</td><td>338.81318</td><td>2.3086258e+04</td><td>1.8320450e+01</td><td>2.9649575e+03</td><td>6.2088137e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.02862</td><td>6.5425027e-04</td><td>338.81318</td><td>7.3958829e-04</td><td>1.3605391e-02</td><td>-2.5300540e-02</td></tr>
    <tr><td>1381.5125760342053</td><td>nan</td><td>nan</td><td>-1.1858977e-03</td><td>110922</td><td>664.01887</td><td>338.81982</td><td>2.3105682e+04</td><td>1.8324867e+01</td><td>2.9604985e+03</td><td>6.2097011e+00</td><td>nan</td><td>nan</td><td>1000000000000000</td><td>nan</td><td>nan</td><td>nan</td><td>nan</td><td>664.01887</td><td>6.5310486e-04</td><td>338.81982</td><td>7.3841790e-04</td><td>3.2073301e-03</td><td>-1.8903004e-02</td></tr>
    </table>



In this table, you are given the time and the flux for your object of
interest. There does however seem to be three entries for flux: flux,
sap_flux, and pdcsap_flux. By default the flux = pdcsap_flux, but what
do these entries mean?

-  **Simple Aperture Photometry (SAP)**: The SAP light curve is
   calculated by summing together the brightness of pixels that fall
   within an aperture set by the *TESS* mission. This is often referred
   to as the *optimal aperture*, but in spite of its name, it can
   sometimes be improved upon! Because the SAP light curve is a sum of
   the brightness in chosen pixels, it is still subject to systematic
   artifacts of the mission.

-  **Pre-search Data Conditioning SAP flux (PDCSAP) flux**: SAP flux
   from which long term trends have been removed using so-called
   Co-trending Basis Vectors (CBVs). PDCSAP flux is usually cleaner data
   than the SAP flux and will have fewer systematic trends.

You can switch between fluxes using the following commands,

::

   pdcsap = lcf[0].pdcsap_flux

   sapflux = lcf[0].sap_flux

Let’s now plot both the pdcsap and sap light curves and see what they
look like.

.. code:: ipython3

    ax = lcf[0].plot(column='sap_flux', normalize=True, label="SAP");
    lcf[0].plot(ax=ax, column='pdcsap_flux', normalize=True, label="PDCSAP");



.. image:: images/TSC2-Intro/output_24_0.png
    :alt: Simple and corrected aperture lightcurves


There are some big differences between these two light curves,
specifically the dips in the SAP light curve and its overall gradent.
These differences are caused by scattered light and other noise issues.
For more information refer to `these
tutorials <https://lightkurve.github.io/lightkurve/tutorials/index.html#removing-instrumental-noise>`__.
For now, let’s think about how we can manipulate the light curves.

2.2.1 Manipulating a light curve:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
-  `bin() <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.LightCurve.bin.html?highlight=bin>`__:
   Reduce the time resolution of the array, taking the average value in
   each bin.

We can use these simply on a light curve object. For this tutorial lets
stick with the PDCSAP flux.

.. code:: ipython3

    ax = lcf[0].plot() 
    ax.set_title("PDCSAP light curve of  L 98-59")




.. parsed-literal::

    Text(0.5, 1.0, 'PDCSAP light curve of  L 98-59')




.. image:: images/TSC2-Intro/output_26_1.png
    :alt: PDCSAP lightcurve


Flattening
^^^^^^^^^^

.. code:: ipython3

    flat_lc = lcf[0].flatten(window_length=401)
    flat_lc.plot();



.. image:: images/TSC2-Intro/output_28_0.png
    :alt: Flattened lightcurve


Folding the light curve
^^^^^^^^^^^^^^^^^^^^^^^

From the `L 98-59 System <https://arxiv.org/pdf/1903.08017.pdf>`__
paper, we know that planet c has a period of 3.690621 days. We can use
the ``fold()`` function to find the transit in our data as shown below.

.. code:: ipython3

    folded_lc = flat_lc.fold(period=3.690621)
    folded_lc.plot();



.. image:: images/TSC2-Intro/output_30_0.png
    :alt: Folded lightcurve


Binning the light curve
^^^^^^^^^^^^^^^^^^^^^^^

Often, to see a trend, it can be beneficial to bin the data, this can be
achieved via the ``bin()`` function.

.. code:: ipython3

    binned_lc = folded_lc.bin(time_bin_size=0.01)
    binned_lc.plot();



.. image:: images/TSC2-Intro/output_32_0.png
    :alt: Folded and binned lightcurve


Great, we can now see our transit very clearly! Note that we can achieve
the same plot from our data using one line of code instead of several,
see below.

``lcf[0].flatten(window_length=401).fold(period=3.690621).bin(time_bin_size=0.01).plot();``

Interact with your light curve
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is also an interactive tool for light curves called
``.interact_bls``. Box Least Squares (BLS), is a method for identifying
transit signals in a light curve.

The ``.interact_bls`` method allows you to identify periodic transit
signals in light curves by manually selecting the period and duration of
the signal.

.. code:: ipython3

    lcf[0].interact_bls()





.. raw:: html

    
    <script id="1002">
      var xhr = new XMLHttpRequest()
      xhr.responseType = 'blob';
      xhr.open('GET', "http://localhost:65219/autoload.js?bokeh-autoload-element=1002&bokeh-absolute-url=http://localhost:65219&resources=none", true);
    
      xhr.onload = function (event) {
        var script = document.createElement('script'),
        src = URL.createObjectURL(event.target.response);
        script.src = src;
        document.body.appendChild(script);
      };
    xhr.send();
    </script>


The light curve in the top right panel is phase-folded with the highest
power period. When you zoom in on a region of period space in the BLS
periodogram, it will automatically update the phase plot with the new
period-at-max-power. Changing the duration using the slider in the
bottom left will also update the BLS periodogram and phase-folded light
curve. Finally, the parameters of the BLS model can be found in the
bottom right panel.

What if your object is not a target of interest but simply observed
within the full framed images? You can still extract the data and create
a 30-min or 10-min cadenced light curve.

2.3 Creating a light curve using FFI data:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In our previous FFI search, we found that *L 98-59* was observed in
Sector 2 with a 30-min cadence. This data is stored as the 2nd argument
of the *search_ffi* array.

To create the light curve from the FFI data, we must first download the
relevant images. Note that we do not want the entirety of the Sector 2
FFI, only a small region surrounding our object of interest. We can
specify the size of the region we want to cut out using the commands
below; in this case we want a 10x10 pixel region.

.. code:: ipython3

    ffi_data = search_ffi[1].download(cutout_size=10)

Let’s now see what this cut out looks like and also check that our
object is at the center of it.

.. code:: ipython3

    ffi_data.plot()




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7f84b36fd0d0>




.. image:: images/TSC2-Intro/output_40_1.png
    :alt: Target pixel file


The above figure indicates the pixels on the CCD camera, with which *L
98-59* was observed. The color indicates the amount of flux in each
pixel, in electrons per second. The y-axis shows the pixel row, and the
x-axis shows the pixel column. The title tells us the *TESS* Input
Catalogue (`TIC <https://tess.mit.edu/science/tess-input-catalogue/>`__)
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

    target_mask = ffi_data.create_threshold_mask(threshold=15, reference_pixel='center')
    n_target_pixels = target_mask.sum()
    n_target_pixels




.. parsed-literal::

    9



This indicates that there are 9 pixels which are above our threshold and
in our mask. We can now check to make sure that our target is covered by
this mask using plot.

.. code:: ipython3

    ffi_data.plot(aperture_mask=target_mask, mask_color='r');



.. image:: images/TSC2-Intro/output_44_0.png
    :alt: target pixel file with target aperture


Nice! We see our target mask centered on the 9 brightest pixels in the
center of the image. Let’s see what the light curve looks like. Note
that this light curve will be uncorrected for any anomalies or noise,
and that the flux is therefore based upon “Simple Aperture Photometry”
(SAP).

To create our light curve we will pass our **aperture_mask** to the
```to_lightcurve`` <https://lightkurve.github.io/lightkurve/reference/api/lightkurve.KeplerTargetPixelFile.to_lightcurve.html?highlight=to_lightcurve>`__
function.

.. code:: ipython3

    ffi_lc = ffi_data.to_lightcurve(aperture_mask=target_mask)

Once again, we can examine the light curve data as a table, but note
this time that there is only one flux value and that as default this is
the SAP flux.

.. code:: ipython3

    ffi_lc




.. raw:: html

    <i>TessLightCurve length=1196 LABEL=&quot;&quot; SECTOR=2</i>
    <table id="table140208687476304" class="table-striped table-bordered table-condensed">
    <thead><tr><th>time</th><th>flux</th><th>flux_err</th><th>centroid_col</th><th>centroid_row</th><th>cadenceno</th><th>quality</th></tr></thead>
    <thead><tr><th></th><th>electron / s</th><th>electron / s</th><th>pix</th><th>pix</th><th></th><th></th></tr></thead>
    <thead><tr><th>object</th><th>float32</th><th>float32</th><th>float64</th><th>float64</th><th>int64</th><th>int32</th></tr></thead>
    <tr><td>1354.1355100037465</td><td>20954.431640625</td><td>3.968478202819824</td><td>664.053236257685</td><td>338.870953330744</td><td>0</td><td>0</td></tr>
    <tr><td>1354.1563430385859</td><td>20953.640625</td><td>3.9688515663146973</td><td>664.0529987132587</td><td>338.87003750094146</td><td>1</td><td>0</td></tr>
    <tr><td>1354.177176075171</td><td>20948.37890625</td><td>3.9678900241851807</td><td>664.0535754626561</td><td>338.8696240269748</td><td>2</td><td>0</td></tr>
    <tr><td>1354.1980091135024</td><td>20953.16796875</td><td>3.9682953357696533</td><td>664.053397969705</td><td>338.86938462421125</td><td>3</td><td>0</td></tr>
    <tr><td>1354.218842153522</td><td>20949.62109375</td><td>3.9680519104003906</td><td>664.05334777157</td><td>338.86842105447164</td><td>4</td><td>0</td></tr>
    <tr><td>1354.239675195171</td><td>20950.841796875</td><td>3.9680023193359375</td><td>664.0529491917277</td><td>338.8680324715659</td><td>5</td><td>0</td></tr>
    <tr><td>1354.260508238421</td><td>20944.640625</td><td>3.9673573970794678</td><td>664.0522733076061</td><td>338.86667562350004</td><td>6</td><td>0</td></tr>
    <tr><td>1354.2813412832716</td><td>20952.73046875</td><td>3.9680874347686768</td><td>664.0519973612013</td><td>338.86666190722457</td><td>7</td><td>0</td></tr>
    <tr><td>1354.302174329665</td><td>20949.45703125</td><td>3.9677042961120605</td><td>664.0511057724311</td><td>338.8659224181862</td><td>8</td><td>0</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>1381.3018854391335</td><td>21803.31640625</td><td>4.048139572143555</td><td>664.009622243243</td><td>338.7804066840283</td><td>1186</td><td>0</td></tr>
    <tr><td>1381.3227185149694</td><td>21763.5703125</td><td>4.044528007507324</td><td>664.0098234495485</td><td>338.7783433746617</td><td>1187</td><td>0</td></tr>
    <tr><td>1381.3435515902245</td><td>21740.970703125</td><td>4.0420989990234375</td><td>664.010488493472</td><td>338.7803301985909</td><td>1188</td><td>0</td></tr>
    <tr><td>1381.364384664897</td><td>21700.6015625</td><td>4.038733005523682</td><td>664.0101843813644</td><td>338.77844460947045</td><td>1189</td><td>0</td></tr>
    <tr><td>1381.385217739045</td><td>21676.36328125</td><td>4.036615371704102</td><td>664.0108564056399</td><td>338.7785207357921</td><td>1190</td><td>0</td></tr>
    <tr><td>1381.4060508126108</td><td>21656.921875</td><td>4.034541606903076</td><td>664.0106157420802</td><td>338.777296648174</td><td>1191</td><td>0</td></tr>
    <tr><td>1381.4268838857115</td><td>21613.62890625</td><td>4.0302863121032715</td><td>664.0110574507974</td><td>338.77740512578055</td><td>1192</td><td>0</td></tr>
    <tr><td>1381.447716958347</td><td>21571.404296875</td><td>4.026115417480469</td><td>664.0115646734967</td><td>338.77744780257865</td><td>1193</td><td>0</td></tr>
    <tr><td>1381.468550030574</td><td>21527.71875</td><td>4.021993160247803</td><td>664.0113081777426</td><td>338.77612574703835</td><td>1194</td><td>0</td></tr>
    <tr><td>1381.4893831023946</td><td>21476.515625</td><td>4.017423152923584</td><td>664.0124305558461</td><td>338.7753083946345</td><td>1195</td><td>0</td></tr>
    </table>



Let’s now plot this.

.. code:: ipython3

    ffi_lc.plot(label="SAP FFI")




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7f84b08b7550>




.. image:: images/TSC2-Intro/output_50_1.png
    :alt: Simple aperture lightcurve


Looking at the above light curve, we can see two dominant peaks and
observe that the flux in the aperture is dominated by what is known as
scattered light. We can tell this because *TESS* orbits Earth twice in
each sector, thus patterns which appear twice within a sector are
typically related to *TESS’* orbit (such as the scattered light effect).

We will discuss this issue in more detail below.

3. How to analyze and assess various data anomalies and how you might visualize them
------------------------------------------------------------------------------------

Lets take a look at the SAP light curves derived from our FFI data and
the PDCSAP light curve derived from our Light Curve File.

.. code:: ipython3

    ax = lcf[0].plot(column='pdcsap_flux', normalize=True, label="PDCSAP");
    ffi_lc.plot(ax=ax, normalize=True, label="SAP FFI")




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7f849105ccd0>




.. image:: images/TSC2-Intro/output_53_1.png
    :alt: Lightcurve comparison


Looking at the figure above, you can see that the SAP light curve has a
long-term change in brightness that has been removed in the PDCSAP light
curve, while keeping the transits at the same depth. For most
inspections, a PDCSAP light curve is what you want to use, but when
looking at astronomical phenomena that aren’t planets (e.g. long-term
variability), the SAP flux may be preferred.

The primary source of noise removed from the SAP light curve is that of
scattered light. Each of TESS’s cameras has a lens hood to reduce the
scattered light from the Earth and the Moon. Due to TESS’s wide field of
view and the physical restrictions of the Sun shade, the lens hood is
not 100% efficient. The effect of the scattered light on the CCD’s can
be seen in the video below.

.. raw:: html

   <video width="100%" height="100%" controls src="ScatteredLight.mov" />

Interactive inspection:
~~~~~~~~~~~~~~~~~~~~~~~

By interactively inspecting the area around your object of interest, you
can see when scattered light comes into play, and also how it effects
the light curve. To do this, we use the ``interact()`` function.

.. code:: ipython3

    ffi_data.interact()





.. raw:: html

    
    <script id="1003">
      var xhr = new XMLHttpRequest()
      xhr.responseType = 'blob';
      xhr.open('GET', "http://localhost:65233/autoload.js?bokeh-autoload-element=1003&bokeh-absolute-url=http://localhost:65233&resources=none", true);
    
      xhr.onload = function (event) {
        var script = document.createElement('script'),
        src = URL.createObjectURL(event.target.response);
        script.src = src;
        document.body.appendChild(script);
      };
    xhr.send();
    </script>


You can move the large bottom left slider to change the location of the
vertical red bar, which indicates which cadence is being shown in the
TPF postage stamp image. The slider beneath the TPF postage stamp image
controls the screen stretch, which defaults to logarithmic scaling
initialized to 1% and 95% lower and upper limits respectively.

You can move your cursor over individual data points to show hover-over
tooltips indicating additional information about that datum. Currently,
the tooltips list the cadence, time, flux, and quality flags. The tools
on the right hand side of the plots enable zooming and pixel selection.

Interaction modes:

-  Clicking on a single pixel shows the time series light curve of that
   pixel alone.
-  Shift-clicking on multiple pixels shows the light curve using that
   pixel mask.
-  Shift-clicking on an already selected pixel will deselect that pixel.
-  Clicking and dragging a box will make a rectangular aperture mask —
   individual pixels can be deselected from this mask by shift-clicking
   (box deselecting does not work).
-  The screen stretch high and low limits can be changed independently
   by clicking and dragging each end, or simultaneously by clicking and
   dragging in the middle.
-  The cadence slider updates the postage stamp image at the position of
   the vertical red bar in the light curve.
-  Clicking on a position in the light curve automatically seeks to that
   cadence number.
-  The left and right arrows can be clicked to increment the cadence
   number by one.
-  The interact() tool works for *TESS* data and *Kepler/K2*.

This tool can also be used to see how crowded the field of your sources
is and if anything else unusual happened during observation.

Interact Sky:
~~~~~~~~~~~~~

*Lightkurve* has an additional tool to interactively inspect target
pixel files — ``.interact_sky``. This method brings up a single frame of
the target pixel file with targets identified by Gaia marked by red
circles. The size of the circle scales with the magnitude of the target,
where brighter sources are larger and fainter sources are smaller. Using
your cursor, you can hover over the red circles to display useful
information from Gaia, including its Gaia ID, G band magnitude, and
coordinates.

.. code:: ipython3

    ffi_data.interact_sky()





.. raw:: html

    
    <script id="1004">
      var xhr = new XMLHttpRequest()
      xhr.responseType = 'blob';
      xhr.open('GET', "http://localhost:65234/autoload.js?bokeh-autoload-element=1004&bokeh-absolute-url=http://localhost:65234&resources=none", true);
    
      xhr.onload = function (event) {
        var script = document.createElement('script'),
        src = URL.createObjectURL(event.target.response);
        script.src = src;
        document.body.appendChild(script);
      };
    xhr.send();
    </script>


.. parsed-literal::

    /Users/rhounsel/opt/anaconda3/envs/astroconda/lib/python3.7/site-packages/lightkurve/interact.py:517: LightkurveWarning: Proper motion correction cannot be applied to the target, as none is available. Thus the target (the cross) might be noticeably away from its actual position, if it has large proper motion.
      category=LightkurveWarning)


This tool is useful for crowded sources.

Cadence Quality Flags:
~~~~~~~~~~~~~~~~~~~~~~

The *TESS* pipeline populates a series of quality flags to indicate when
a cadence may have been taken during an anomalous event. These flags are
available in the Light Curve Files, the Target Pixel Files, and a subset
are available for the FFIs.

Aperture Mask Image Flags:
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Light Curve Files and Target Pixel Files contain an image in the
**APERTURE FITS** extension that describes how each pixel was used in
the processing.

Tables of these flags can be found
`here <https://outerspace.stsci.edu/display/TESS/2.0+-+Data+Product+Overview#id-2.0DataProductOverview-Table:CadenceQualityFlags>`__,
where a description of each flag is provided.

Additional Resources
--------------------

In this tutorial, we have covered the basics of how to obtain, reduce
and analyze *TESS* data using *Lightkurve*. We have, however, only
skimmed the surface of what *Lightkurve* can do and how to investigate
the data. For more detailed tutorials as well as other useful tools,
please visit the following pages.

-  `Lightkurve Tutorials
   page <https://lightkurve.github.io/lightkurve/tutorials/index.html#tutorialsl>`__: A set of
   21 tutorials dealing with Kepler/K2 and TESS data
-  `TESS GI data products
   page <https://heasarc.gsfc.nasa.gov/docs/tess/data-analysis-tools.html>`__:
   A set of 7 TESS specific tutorials.
-  `STScI Kepler K3
   notebooks <https://github.com/spacetelescope/notebooks/tree/master/notebooks/MAST/Kepler>`__:
   A set of notebooks produced by a collaboration between NumFocus,
   MAST, *Lightkurve*, and TESS GI office. They make use of python
   astronomical data packages to demonstrate how to analyze time series
   data from these NASA missions. New tools are presented here and
   techniques for the advanced user.
