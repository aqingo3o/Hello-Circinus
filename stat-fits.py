'''
輸入檔案路徑，就能用 能casatasks.imstat() 估計 RMS 的方法演示
算一種即食函式
沒什麼技術含量，就是方便我用而已
寫成函式因為他可以清掉過程中的 .im們
'''
from casatasks import importfits, imstat, exportfits
import shutil

def Stat_fits(pathIN, chans) :
    importfits(fitsimage=pathIN, imagename='casaIN.image', overwrite=True)
    print('tataima!') 
    the_stats = imstat('casaIN.image', chans=chans)
    print('RMS =', the_stats['rms'], 'Jy/beam')
    print('Use "print(the_stats[strr])" to get other stats info')
    shutil.rmtree('casaIN.image')
    print()
    print('All metafiles have been cleaned')
    return the_stats

# Demo
pathIN = '/Users/aqing/Documents/1004/Circinus_galaxy/Ratio-Map/mvp_smoothFirst/cube_smoothed/HCN-1-0_cube_smoothed-4545.fits'
chans = '1854~1858' 
Stat_fits(pathIN, chans)

'''
error{
data_update: path must exist as a directory and it must be owned by the user, path = /Users/aqing/.casa/data
Warning: measurespath must exist as a directory and it must be owned by the user.
Warning: no auto update is possible on this measurespath by this user.}

這種 error message 好常見誒
明明之前解決過了操
反正就給他建一個資料夾就好(?)

'''
