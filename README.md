# TESS Website 
***The website for astronomers using NASA's TESS space telescope.***

Live URL: 

Test URL: http://Nschanche.github.io/TSSCWebsite/


## Quickstart



## Detailed instructions for website editors



## Makefile tasks

The Makefile provides the following useful commands:
* `make html` to compile *all pages* and store them under `output/`.
* `make quick` to compile *only pages that have changed*.  This is faster than `make html` but will cause the front and news pages to be incomplete.
* `make devserver` to start a development webserver on your local machine at `http://localhost:8000`, which will auto-compile a page when you make a change. This too causes the frontpage to be empty unless you call `make html`.
* `make github` to send the compiled HTML files to the [development server](http://tessgi.github.io/TessGiWebsite/).

Note: `make quick` and `make devserver` both use agressive caching which allows the website to be built quickly, but causes the listing of news items to be missing from the front page (`output/index.html`).  You need to call `make html` if you care about a preview of the front page. Calling `make github` or `make live` automatically triggers `make html`.


## Authors

This site started off as the Kepler/K2 website, created by Thomas Barclay, Geert Barentsen, and Knicole Colón for the Kepler/K2 Guest Observer Office at NASA Ames.

The current TSSC website is developed and maintained by Christina Hedges, Nicole Schanche, Veselin Kostov, Tyler Pritchard, and Rebekah Hounsell at NASA Goddard.

Created using the [Pelican package](getpelican.com) and the
[pelican-bootstrap3 theme](https://github.com/DandyDev/pelican-bootstrap3).


