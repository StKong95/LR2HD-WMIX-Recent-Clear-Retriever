# Lunatic Rave 2 HD Recent Clear Retriever

This script reads text from screenshots of Lunatic Rave 2 WMIX HD's result screen. It retrieves information such as clear type and song level from the image. The information will be stored in a text file within the same directory. It will continue to do so in real time as more images are created.

It is not meant for fail result screens.

- Version: **1**
- Licensed under: **GPLv3**

## Requirements
- [WMIX HD Skin](https://onedrive.live.com/?authkey=%21AJDT%5FQWX9IJttnU&id=E92E2372413C5A12%21387&cid=E92E2372413C5A12)
- [OpenCV ](https://pypi.org/project/opencv-python/)
- [PyTesseract](https://pypi.org/project/pytesseract/)
- [watchdog](https://pypi.org/project/watchdog/)

## Instructions
1) Place the script in the base directory of Lunatic Rave 2 HD.
2) Run script.
3) Take screenshots of scores on WMIX HD's result screen.
4) Information will be stored in recent.txt located in the same directory.

## 4 Screenshots Example
#recent.txt
```RECENT
st3 NC
sl10 HC
st0 HC
SP02 FC
```