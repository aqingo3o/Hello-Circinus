'''
輸入檔案路徑和 n 個 channel 區間(在 chansL 中)
就會輸出由 n 個區間算得的 rms 值的平均。
沒什麼技術含量，就是方便我用而已
'''
from casatasks import importfits, imstat
import numpy as np
import shutil

#
commonPath = '/Users/aqing/Documents/1004/Circinus_galaxy/Ratio-Map/mvp_smoothFirst/1_cube_smoothed/'
parti_fileName = ['HCN-1-0', 'HCO+-1-0', 'CN-J12-12', 'CN-J32-12', 'HNC-1-0', 'CS-J2-1']
# 因為CO 的空白裁掉了，不確定怎麼用，所以就沿用之前的估計...
chansL = [['1063~1067', '2624~2628', '1854~1858'], # HCN(1-0)
          ['1063~1067', '2624~2628', '1854~1858'], # HCO+(1-0)
          ['1757~1761', '2456~2460', '3596~3600'], # CN(J1/2-1/2)
          ['368~372', '3022~3026', '1797~1801'], # CN(J3/2-1/2)
          ['1574~1578', '2069~2073', '3238~3242'], # HNC(1-0)
          ['1201~1205', '2494~2499', '2626~2630'] # CS(J2-1)
          ]

# Do the cacu
for n in range(len(parti_fileName)):
    rms = []
    pathIN = f'{commonPath}{parti_fileName[n]}_cube_smoothed-4545.fits'
    importfits(fitsimage=pathIN, imagename='casaIN.image', overwrite=True)
    for i in chansL[n] :
        the_stats = imstat('casaIN.image', chans=i)
        rms.append(the_stats['rms'])
    print(rms)
    print(f"!!! {parti_fileName[n]}'s RMS = {np.average(rms)} Jy/beam !!!")
    shutil.rmtree('casaIN.image')
    print('All metafiles have been cleaned', end='\n\n')

    print('FIN')