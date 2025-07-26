# Ratio-Map
Exploring potential scientific insights using final science-ready data products. Calibration and imaging were performed beforehand and are not included here.  
This project is part of the Academia Sinica Institute of Astronomy and Astrophysics (ASIAA) Summer Student Program.  
這邊先跪下來感謝忙得要死還一天一咪的老豆、讓我能參加 ssp 的金主&&瘋狂投餵我們的朱有花老師以及**這方面的專家**林俐暉老師  
(還有幫我們在 PC 上 casa 裝到好的 cchelp 和搖人來修 carat 的對面老哥 supervisor)
>
- 任何人可以幫助我的破爛電波天文學/程式/數據處理/大腦/使用 github，我都會跪下來感謝您的。  
- 然後我現在知道我 commit message 都在亂寫了啊啊呃算了  
- 對於我的檔案結構是一坨（）我感到非常抱歉
>
**⚠️ This repo mainly serves as a personal log of the research process and may contain contain many imperfect operations .**  
>
---
## Tools
- CASA 6.4.1
- modular CASA (with Rosetta2)
- CARTA v5.0.0 beta.1
- python3.10
- astropy
- matplotlib, numpy
## Recommended scripts
Overtime, bigger number newer script.  
（好的東西會是很多流水線的湯底...  
1. py_HCN-CO_ifelLarger.ipynb
2. HCN-CO_wask/py_HCN-CO_wask_v2.ipynb

---
### mom0_smoothFirst/
Results or codes that do imsmooth() on data cubes first  
then generate moment maps will be placed here.
##
### The .py(s) under Ratio-map/
Some costum functions/scripts  
maybe useless or maybe useful?  
afraid they would disappear in my messy ~/  
so I pushed them.
##
### HCN-CO_wask/
Do imsmooth() on mom0 that made in CARTA,  
then regrid, reconvol(<- that's actually wrong) and generate ratio map.  
Seems to be incorrect workflow so I just closed this case.
##
### py_oldData.ipynb under Ratio-map
Scripts I used when trying to reproduce the data processing of paper(Wilson et al. 2023).
