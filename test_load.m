clear
clc
A = load('test.txt');
mycolor = ExtractColormap(1024);
figure; imagesc(A);colormap(mycolor);