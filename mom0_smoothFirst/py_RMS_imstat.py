'''
輸入檔案路徑和 n 個 channel 區間(在 chansL 中)
就會輸出由 n 個區間算得的 rms 值的平均。
沒什麼技術含量，就是方便我用而已
'''
from casatasks import importfits, imstat
import numpy as np
import shutil

def Stat_fits(pathIN, chans) :
    importfits(fitsimage=pathIN, imagename='casaIN.image', overwrite=True)
    #print('tataima!') 
    the_stats = imstat('casaIN.image', chans=chans)
    #print('RMS =', the_stats['rms'], 'Jy/beam')
    #print('Use "print(the_stats[strr])" to get other stats info')
    shutil.rmtree('casaIN.image')
    print('All metafiles have been cleaned')
    return the_stats

# Do the cacu
pathIN = '/Users/aqing/Documents/1004/Circinus_galaxy/Ratio-Map/mvp_smoothFirst/cube_smoothed/HCN-1-0_cube_smoothed-4545.fits'
chansL = ['1063~1067', '2624~2628', '1854~1858'] # HCN(1-0)
'''
pathIN = '/Users/aqing/Documents/1004/Circinus_galaxy/Ratio-Map/mvp_smoothFirst/cube_smoothed/CN-J12-12_cube_smoothed-4545.fits'
chansL = ['1757~1761', '2456~2460', '3596~3600'] # CN(J12-12)

pathIN = '/Users/aqing/Documents/1004/Circinus_galaxy/Ratio-Map/mvp_smoothFirst/cube_smoothed/HNC-1-0_cube_smoothed-4545.fits'
chansL = ['1574~1578', '2069~2073', '3238~3242'] # HNC(1-0)
'''
rms = []
for i in range(len(chansL)) :
    the_stats = Stat_fits(pathIN, chansL[i])
    rms.append(the_stats['rms'])
print()
print(rms)
print(f'!!! RMS = {np.average(rms)} Jy/beam !!!')