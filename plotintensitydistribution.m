function plotintensitydistribution(sys, X, Y, I)
Imax=max(max(I));
I = I./Imax; % Normalise I with the peak intensity in the focal region
Id = imresize(I,[1080,1080]); % Enhance the resolution of the image
imagesc(X./sys.wl,Y./sys.wl,Id);
colormap jet(256)
colorbar
axis equal
axis tight
end
    