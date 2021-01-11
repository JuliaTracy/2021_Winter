setwd("C:/Users/Apple/Desktop")
data = read.csv("2-7.csv")
x = data[,1]
y = data[,2]
n = length(x)
plot(x,y,pch = 16)
title(main="Êý¾ÝÉ¢µãÍ¼")