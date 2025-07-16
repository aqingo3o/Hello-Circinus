'''
方便的用 imsmooth() 處理 FITS 的函式
應該是不會拉屎
建議以變數傳入 pathIN, tarBeam, fitsOUT
需要 casatasks
小心使用！！
'''
from casatasks import importfits, imsmooth, exportfits
import os
import shutil

shutil.rmtree('/folder_name')
def Do_smooth(pathIN, kernel, tarBeam, fitsOUT) :
    importfits(fitsimage=pathIN, imagename='casaIN.image', overwrite=True) 
    imsmooth(imagename='casaIN.image', outfile='casa_OUT.image', kernel=kernel, beam=tarBeam, overwrite=True)
    exportfits(imagename='casa_OUT.image', fitsimage=fitsOUT, overwrite=True)
    shutil.rmtree('/casaIN.image')
    shutil.rmtree('/casaOUT.image')


# for example
CO_path = '/Users/aqing/Documents/1004/Circinus_galaxy/Ratio-Map/mvpData/CO(1-0)_mom0_2.2sigma.fits' # 起到一個增加可讀性的功能？
CO_out = 'CO22_imsmooth33'
tarBeam = {'major': '3arcsec', 'minor': '3arcsec', 'pa': '0deg'}
Do_smooth(CO_path, 'g', tarBeam, CO_out)