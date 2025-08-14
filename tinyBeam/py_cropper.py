import numpy as np
import shutil

# 因為是給 full CASA 的腳本
# 所以沒有 import casatasks

'''
一種 cube 工廠
會做裁切和改寫標頭 (restfreq)
建議以變數傳入 pathIN, tarBeam, fitsOUT

parameters:
pathIN (str)   : 原來那cube 的檔案位置
channel (str)  : 要切的範圍，由人類手工決定，中間的連接符是波浪號
fitsOUT (str)  : 輸出檔案的名字，雖然很意外但不可以包含括號
f0 (number)    : 要修改的 rest frequency，單位是 Hz，這邊輸入數字，函式裡面有轉字串的部分了
'''


def Cube_factory(pathIN, channel, f0, fitsOUT) : # 裁切和改寫標頭，沒有卷積
    importfits(fitsimage=pathIN, imagename='casaIN.image', overwrite=True) 
    print('tataima!')
    imsubimage(imagename='casaIN.im', outfile='casaOUT.im', chans=channel)
    print('Done crop.')
    imhead(imagename='casaOUT.image', mode='put', hdkey='restfreq', hdvalue=str(f0)) # 資料型態竟然要是字串，不客氣，幫轉了
    print(f"Header keyWord 'RESTFREQ' now is {f0/1e9} GHz") 
    exportfits(imagename='casaOUT.image', fitsimage=fitsOUT, overwrite=True)
    shutil.rmtree('casaIN.image')
    shutil.rmtree('casaOUT.image')
    print('Metafiles cleaned')

commonPath = 'a'/  # 這邊應該填入大電腦的路徑
moleL = [('3_HCO+-1-0_beam2.89_CDWilson', '370~415', 8.9188E+10), ##
         ('5_HCO+-2-1_beam1.32_MVP', '1200~1685', 1.78345E+11),
         ('6_CO-2-1_beam0.39_MVP', '25~775', 2.30538E+11), # 這個切過了，就是這麼大
         ('6_HCO+-3-2_beam1.47_CDWilson', '135~195', 2.67558E+11),
         ('7_HCO+-4-3_beam0.29_Izumi2018', '280~405', 3.56734E+11),
         ('7_CO-3-2_beam0.29_Izumi2018', '165~315', 3.45796E+11)]


for mole, c, fr in moleL:
    pathIN = f'{commonPath}cube_band{mole}.fits'
    out = f'cube_band{mole}_cropped.fits'
    Cube_factory(pathIN, c, fr, out)