'''
this script must go with the venv (astro_py310)
or any environment that have astropy and radio-beam

他媽的動起來很有問題欸
'''

import matplotlib.pyplot as plt
from astropy.io import fits
from astropy import units as u 
from astropy.convolution import convolve_fft
from radio_beam import Beam
from astropy.wcs import WCS
import numpy as np

# 存檔芝士
def Save_as_FITS(the_file_name, ima_data, ref_header, ref_beam, beam_a_Beam): 
    the_file_name = the_file_name + '.fits'
    the_header = ref_header.copy() # new header 是複製一個已知 header 的大部分...
    if beam_a_Beam == True: # ref_beam 是實際意義上的 Beam 的話
        the_header['BMAJ'] = ref_beam.major.to(u.deg).value
        the_header['BMIN'] = ref_beam.minor.to(u.deg).value
        the_header['BPA'] = ref_beam.pa.to(u.deg).value
    else: # ref_beam 是一個 header 的話
        the_header['BMAJ'] = ref_beam['BMAJ']
        the_header['BMIN'] = ref_beam['BMIN']
        the_header['BPA'] = ref_beam['BPA']
    fits.writeto(the_file_name, ima_data, the_header, overwrite=True)
    print(f'Successfully saved a new FITS file as {the_file_name}')


# do the CC
ur_hdul = fits.open('/Users/aqing/Documents/1004/Circinus_galaxy/Ratio-Map/mvpData/CO(1-0)_mom0_2.2sigma.fits') #
ur_header = ur_hdul[0].header
ur_ima = ur_hdul[0].data.squeeze()
ur_beam = Beam.from_fits_header(ur_header)
#pixelScale = abs(ur_header['CDELT1'])*u.arcsec ## 不知道是不是這樣寫
pixelScale = 1.5*u.arcsec

beamPara = [3, 3, 0] # BMAJ, BMIN, BPA
tarBeam = Beam(major=beamPara[0]*u.arcsec, minor=beamPara[1]*u.arcsec, pa=beamPara[2]*u.deg)

bb = f'{beamPara[0]}{beamPara[0]}'
kernel = tarBeam.as_kernel(pixscale=pixelScale)
ur_ima_convl = convolve_fft(ur_ima, kernel)

print('initial ', ur_beam)
print('THE ', tarBeam)
print()
print(f"kernel shape: {kernel.shape}")
print(f"image shape: {ur_ima.shape}")
print('** if ur kernel is so much bigger than image, you will get 一坨 :-(')
print()
print('Successfully convolved the image !')


# pre-view with MPL
plt.figure()
plt.subplot(projection=WCS(ur_header, naxis=2))
plt.imshow(ur_ima_convl, origin='lower', cmap='jet', vmin=0, vmax=np.nanpercentile(ur_ima_convl, 90))
#plt.imshow(ratioMap, cmap='jet') #inferno
#plt.imshow(ratioMap, origin='lower', cmap='jet', vmin=0, vmax=0.28)
plt.colorbar()
plt.xlabel('RA')
plt.ylabel('Dec')
plt.show()


# save as FITS
Save_as_FITS('ttt', ur_ima_convl, ur_header, ur_beam, True)
