clear
close all
sys = systempra;
% colormap jet(256)
X = linspace(-sys.r,sys.r,sys.re);
Y = linspace(-sys.r,sys.r,sys.re);
R = linspace(-sys.r,sys.r,sys.re); % Define R coordinates for the R-Z plane calculation
Z = linspace(-sys.z,sys.z,sys.re); % Define Z coordinates for the R-Z plane calculation
ang = 0;
re2 = 210;
R2 = linspace(-sys.r,sys.r,re2); % Define R coordinates for the R-Z plane calculation
Z2 = linspace(-sys.z,sys.z,re2); % Define Z coordinates for the R-Z plane calculation
[Ix, Iy, Iz, I] = IPSF_Vectorial_Linear_xy(sys, X, Y);
% [Er, Ez, Ix, Iy, Iz, I] = IPSF_Vectorial_radial_rz(sys, R, Z,ang);
% [Ex, Ey, Ez, Ix, Iy, Iz, I] = IPSF_Vectorial_Linear_rz(sys, R, Z,ang);
% [Ex, Ey, Ez, Ix, Iy, Iz, I] = IPSF_Vectorial_circular_rz(sys, R, Z,ang);
% [Ex, Ey, Ez, Ix, Iy, I] = IPSF_Vectorial_azimuthal_rz(sys, R, Z,ang);
figure(1)
imagesc(X./sys.wl,Y./sys.wl,I);
mycolor = ExtractColormap(1024);
colormap(mycolor);
colorbar
xlabel('x(/lambda)');
ylabel('y(/lambda)');
[x, y]=meshgrid(X,Y);
[r, z]=meshgrid(R,Z);
% quiverc(x,y,Ex,Ey);
% axis equal
% axis tight
% [Er2, Ez2, Ix2, Iy2, Iz2, I2] = IPSF_Vectorial_radial_rz(sys, R2, Z2,ang);
[Ex2, Ey2, ~, Ix2, Iy2, Iz2, I2] = IPSF_Vectorial_Linear_rz(sys, R2, Z2,ang);
% [Ex2, Ey2, Ez2, Ix2, Iy2, Iz2, I2] = IPSF_Vectorial_circular_rz(sys, R2, Z2,ang);
% [Ex2, Ey2, Ez2, Ix2, Iy2, I2] = IPSF_Vectorial_azimuthal_rz(sys, R2, Z2,ang);
Ez2 = zeros(length(R2),length(Z2)); % create Ez component for azimuthal only
Er2 = Ex2;
% Er2 = imresize(Er,[re2 re2]);
% Ez2 = imresize(Ez,[re2 re2]);
[r2, z2]=meshgrid(R2,Z2);
Er2(r2<0)=-Er2(r2<0);
figure(2)
imagesc(R./sys.wl,Z./sys.wl,I2);
mycolor = ExtractColormap(1024);
colormap(mycolor);
colorbar
xlabel('x(/lambda)');
ylabel('z(/lambda)');
% hold on
% quiverc(r2,z2,Er2,Ez2);
% axis equal
% axis tight
% hold off
