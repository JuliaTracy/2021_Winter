# 2021_Winter
This repository displays what Julia Li have explored herself since she became an undergraduate.

***Class1 Visualization***
During the epidemic last winter, Julia Li made many attempts to make the COVID-19, which we were all concerned about, more vividly shown in front of our eyes.
Thus, she tried to learn some python libraries like matplotlib, mpl_toolkits.mplot3d, turtle, pyecharts and so on. Although they may be too childish for a large number of people, I was really exited to discover a brand new world, which is exotic and amazing.
1. 2D_virus.py: display the viration of the detected patients in China from Jan to Feb in 2020
2. death&recovered.py: display how many people died and recovered during a short period of time
3. dog.py: draw a cute dog to enlighten people
4. heart.py: draw a adorable heart to show love
5. world.py: show how COVID-19 affected the entire world
6. virus.py: display the detected, the recovered and the died in 3D form
7. SIR.py: use SIR model to predict how the epidemic would spread
8. risk.py: hospitalisation fatality risk from Jan 20th to Feb 12th
9. map.py: show a map of detected person and the flight routes to and from Wuhan

Other tries not related to COVID-19: (for environmental anlysis mostly)
1. polifit.py: just tried how to do statistics in python hhh
2. Beijing&Tianjin.py: AQI of Beijing and Tianjin in 2019
3. Beijing_PM2.5.py, Hebei_PM2.5.py: PM2.5 of Beijing,Tianjin in 2019(viration)
4. Beijing_Season.py, Shijiazhuang_Season.py: how PM2.5 level changes in different seasons in Beijing, Shijiazhuang
5. PM2.5_JJJ.py: comparison of PM2.5 level among Beijing, Tianjin and Shijiazhuang in 2019
6. 北京.py, 天津.py, 河北.py: maps showing how PM2.5 disperse in different areas of BTH
7. Character.py: use turtle to write several vivid characters

***There are also some visualisation programs made by R that has similar functions as the contents above, which I store them in "R Creation" directory. In addition, some Origin programs can draw beautiful pictures as well, thus I include two opju programs here.

***Class2 File Process***
It is really hard for me who are not quite familiar with Microsoft to deal with a large quantities of files and data. In order to improve my efficiency, I wrote/cited some codes to handle file types like excel, csv, nc and so on. Some of codes I have created are as follows.
1. convert.py: convert all xls files in a directory into csv files
2. csv1.py: a framework of reading csv files
3. excel_combine,py: combine 2 xls files and save them to a csv
4. excel_split.py: split 1 xls file into several xls files
5. filemove.py: move the files you assigned from one directory to another
6. ncread.py: a framework of reading nc files
7.ppt.py, ppt2pdf.py: convert ppt/pptx to pdf
8. WWTPsloc.py: compare the information from 2 xls files and merge the records that have same values together
9. rename.py: rename the files in a directory into a more standardized form
10. row.py: count how many rows are there in each txt files in a directory (importing os)

***Class3 Games***
I loved to play computer games when I was a primary-school girl. As I grew up gradually, I do not find it very interesting, probably because I have found something more attractive like chatting with my friends, watching movies and so on. But I do think that creating a small-scaled games on computers by your own is not only entertaining but also fascinating. Using Matlab and Python, the following projects are partially made by myself.
1. ball.py: it is a small game simulate a ball which will crash the bricks laying above it, and users can move mouse to control hos the ball will rebound
2. jigsaw.m: a simple puzzle that has 9 grids and 8 pieces, you can move 1 piece to the empty grid and finally get an intact picture.
3. wuziqi.m: use upper, lower, left and right keys as well as space to control the move of chess pieces. You can play with a friend to see whether you can win.

***Class4 Web-Crawler***
These projects are mainly developed by importing libraries like requests, bs4,

***Class5 Others***
I have off-the-wall ideas sometimes and then I will learn from the Internet to develop something of different categories. They may include tiny open-cv programs, 
1. OCR.py: utilize Baidu API to scan a picture and transform it into text
2. translate_sentencebysentence.py: utilize Baidu Translate API to translate from Chinese to English
3. translate_file2file.py: read a txt file in English and translate it into another file in Chinese
4. face.py: use opencv-python to recognize a face/faces in a photo
5. Email.py: use python to send a QQ Email (smtp.qq.com)
6. POI.py: utilize Baidu API to get information like locations, address, name of the point of interests you assigned
7. zhiwang.py: simulate Google chrome to search for the basic information of thesis on CNKI
8. BPtest.m: a trial to use Back-Propagation neutral network to predict the traffic flow
