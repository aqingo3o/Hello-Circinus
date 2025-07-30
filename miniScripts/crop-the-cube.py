import numpy as np
import shutil

pathIN = '/data/MUSE_cube/ADP.2016-06-14T18_02_17.657.fits'
importfits(fitsimage=pathIN, imagename='casaIN.im', overwrite=True)
print('import=y')

channL = [('84~104','4861H-b'), ('200~220', '5007OIII'), ('1432~1492', '6563H-a')]
for c, n in channL:
    outfile = f'{n}.fits'
    imsubimage(imagename='casaIN.im', outfile='casaOUT.im', chans=c)
    print(11)
    exportfits(imagename='casaOUT.im', fitsimage=outfile, overwrite=True)
    shutil.rmtree('casaOUT.im')

shutil.rmtree('casaIN.im')
print('DONE')
