# QT examples

https://www.qt.io/

We will choose Open Source version
https://www.qt.io/download

![QT](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Qt_logo_2016.svg/175px-Qt_logo_2016.svg.png)

Official bindings now are PySides (PyQT still works too)
https://wiki.qt.io/Qt_for_Python

![PySides](https://qt-wiki-uploads.s3.amazonaws.com/images/3/33/Py-128.png)

## Installation
* https://pypi.org/project/PySide2/

    `pip install PySide2`
    
on windows you might need to set QT_PLUGIN_PATH enviroment variable

(use Win-X then Y then Back search for Advanced System settings - the old ones! -> Enviroment Variables 
create new System Enviroment Variable

`QT_PLUGIN_PATH `
value:
`C:\ProgramData\Anaconda3\Library\plugins\platforms`

C:\ProgramData\Anaconda3\Library\plugins\platforms
should contain the following files:

    `qdirect2d.dll
    qminimal.dll
    qoffscreen.dll
    qwebgl.dll
    qwindows.dll`

If some .dlls are missing you can copy them from 
\Anaconda3\Lib\site-packages\PySide2\plugins\platforms\
to \Anaconda3\Library\plugins\platforms\

Ref: https://stackoverflow.com/questions/41994485/error-could-not-find-or-load-the-qt-platform-plugin-windows-while-using-matplo

## QT Designer 
We do not need to create widgets by hand

https://stackoverflow.com/questions/37419138/is-qt-designer-bundled-with-anaconda



    

