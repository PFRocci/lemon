.. LEMON documentation master file, created by
   sphinx-quickstart on Mon May  6 12:08:02 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

LEMON: differential photometry
==============================

LEMON is a scientific pipeline, written in Python_, that determines the changes in the brightness of astronomical objects over time and compiles their measurements into `light curves`_. The aim of this program is to make it possible to completely **reduce thousands of FITS images of time series** in a matter of only a few hours, requiring minimal user interaction.

For example, to get the light curve of a transit of HAT-P-16b_:

::

    $ lemon astrometry data/*.fits HAT-P-16/
    $ lemon mosaic HAT-P-16/*.fits HAT-P-16-mosaic.fits
    $ lemon photometry HAT-P-16-mosaic.fits HAT-P-16/*.fits phot.LEMONdB
    $ lemon diffphot phot.LEMONdB curves.LEMONdB

The above commands produce, among many others, the following plot:

.. only:: html

    .. thumbnail:: _static/HAT-P-16b-2014-10-31.svg
        :title: The light curve of a transit of exoplanet HAT-P-16b

.. only:: latex

    .. image:: _static/HAT-P-16b-2014-10-31.jpg

LEMON aims at taking most of the burden out of the astronomer, working out of the box with any set of images that conform to the `FITS standard`_. In most scenarios, the above four commands are enough to generate the high-precision light curves of all your astronomical objects.

.. _Python: https://www.python.org/
.. _light curves: https://en.wikipedia.org/wiki/Light_curve
.. _HAT-P-16b: http://exoplanet.eu/catalog/hat-p-16_b/
.. _FITS standard: http://fits.gsfc.nasa.gov/fits_standard.html

User Guide
==========

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart
