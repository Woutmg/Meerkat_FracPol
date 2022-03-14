import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as colors

import scipy.constants as c
from scipy import stats

from astropy.utils.data import get_pkg_data_filename
from astropy.wcs import WCS
from astropy import wcs
from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from astropy import units as u

import bdsf

directory_univ_mkt = r'/net/vdesk/data2/GoesaertW/Meerkat_Data/Abell_85/'
img = bdsf.process_image(directory_univ_mkt+'Abell_85_Linpol_Freqmean.fits')
img.export_image('Abell85_ch0_BDSF_output.fits', img_type='ch0')
img.export_image('Abell85_rms_BDSF_output.fits', img_type='rms')
img.export_image('Abell85_mean_BDSF_output.fits', img_type='mean')
img.export_image('Abell85_gaus_model_BDSF_output.fits', img_type='gaus_model')
img.export_image('Abell85_gaus_resid_BDSF_output.fits', img_type='gaus_resid')

img.write_catalog('Abell85_catalog_BDSF_output.fits', catalog_type='gaul')


