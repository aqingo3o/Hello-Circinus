# Ratio-Map
Making ratio maps of some moleculars in Circinus Galaxy with asrtopy (and modular CASA, maybe)

>
任何人可以幫助我的破爛電波天文學/程式/數據處理/大腦/使用 github，我都會跪下來感謝您的。  
然後我現在知道我 commit message 都在亂寫了啊啊呃算了
>
---
## Recommended scripts
Overtime, bigger number newer script.  
好的東西會是很多流水線的湯底...  
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
