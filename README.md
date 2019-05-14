# amap-location-to-lnglat
使用高德地图api批量转换地址为经纬度
- PyQt5
- pandas
- requests
- qdarkstyle

1. 软件界面框架使用PyQt5，并使用QThread多线程，将界面线程与执行线程分离，保证在进行转换时界面不阻塞；
2. 转换过程调用高德地图api，需自行申请key，并替换[此处key值](https://github.com/MacwinWin/amap-location-to-lnglat/blob/29f1d4d0b52c6a98785ccb4357a3fc60c0b328ea/module/thread.py#L33);
3. 界面美化使用qdarkstyle

<img src="https://github.com/MacwinWin/amap-location-to-lnglat/blob/master/locationConvert.gif">
