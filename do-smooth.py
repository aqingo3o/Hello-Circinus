'''
方便的用 imsmooth() 處理 FITS 的函式
應該是不會拉屎
建議以變數傳入 pathIN, tarBeam, fitsOUT
需要 casatasks
小心使用！！
'''
from casatasks import importfits, imsmooth, exportfits
import shutil

def Do_smooth(pathIN, kernel, tarBeam, fitsOUT) :
    importfits(fitsimage=pathIN, imagename='casaIN.image', overwrite=True) 
    imsmooth(imagename='casaIN.image', outfile='casaOUT.image', kernel=kernel, beam=tarBeam, targetres=True, overwrite=True)
    exportfits(imagename='casaOUT.image', fitsimage=fitsOUT, overwrite=True)
    shutil.rmtree('casaIN.image')
    shutil.rmtree('casaOUT.image')
    print('clean metafiles')


# for example
CO_path = '/Users/aqing/Documents/1004/Circinus_galaxy/Ratio-Map/mvpData/CO(1-0)_mom0_2.2sigma.fits' # 起到一個增加可讀性的功能？
CO_out = 'CO22_imsmooth33'
tarBeam = {'major': '3arcsec', 'minor': '3arcsec', 'pa': '0deg'} # 預設「卷積到目標解析度(targetres)」為預設
Do_smooth(CO_path, 'g', tarBeam, CO_out)
