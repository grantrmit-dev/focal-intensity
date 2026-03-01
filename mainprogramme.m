%-------Mainprogram for the vectorial Debye calculation for a high NA objective-------
%% Setting system prameters for the calculation
clc
sys = systempra;
fprintf('Wavelength is %u nm.\n',sys.wl.*1e9);
fprintf('Numerical-aperture of the objective is %1.1f.\n',sys.NA);
if sys.e==0
     fprintf('Circular aperture.\n');    
else
     fprintf('The radius of the annular aperture is %1.1f.\n',sys.e);
end
if sys.m==0;
     fprintf('Planewave incident beam.\n');
else
     fprintf('The topological charge of the phase vortex is %1.0f.\n',sys.m);
end

%% Define the space of the calculation by using the system prameters
R = linspace(-sys.r,sys.r,sys.re); % Define R coordinates for the R-Z plane calculation
Z = linspace(-sys.z,sys.z,sys.re); % Define Z coordinates for the R-Z plane calculation
X = linspace(-sys.r,sys.r,sys.re); % Define X coordinates for the X-Y plane calculation
Y = linspace(-sys.r,sys.r,sys.re); % Define y coordinates for the X-Y plane calculation

%% Debye integral calculations 
%-------------Linear polarisation--------------
if strcmp(sys.P, 'Linear') % Use if case to decide to polarization states then using the right program
    fprintf('Incident beam is linearly polarised.\n');
    if strcmp(sys.plane, 'X-Y')
        fprintf('Calculation of the intensity distribution in the X-Y plane at z=%1.1f micron...\n', sys.z0*1e6);
        [Ix Iy Iz I] = IPSF_Vectorial_Linear_xy(sys, X, Y); % Ix, Iy,Iz,I are intensity distribution of 
                                                                  % the field components 
    elseif strcmp(sys.plane,'R-Z')
         fprintf('Calculation of the intensity distribution in the R-Z plane... \n');
        [Ixxz Iyxz Izxz Ixz] = IPSF_Vectorial_Linear_rz(sys, R, Z,0);% 'X-Z' plane
        [Ixyz Iyyz Izyz Iyz] = IPSF_Vectorial_Linear_rz(sys, R, Z,pi/2);% 'Y-Z' plane for linear polarisation only
    end
    
%-------------Circular polarisation--------------
elseif strcmp(sys.P, 'Circular') 
    fprintf('Incident beam is circularly polarised.\n');
    if strcmp(sys.plane, 'X-Y')
        fprintf('Calculation of the intensity distribution in the X-Y plane at z=%1.1f micron...\n', sys.z0*1e6);
        [Ix Iy Iz I] = IPSF_Vectorial_circular_xy(sys, X, Y);
    elseif strcmp(sys.plane, 'R-Z')
         fprintf('Calculation of the intensity distribution in the R-Z plane... \n');
        [Ixrz Iyrz Izrz Irz] = IPSF_Vectorial_circular_rz(sys, R, Z,0);
    end
    
%-------------Radial polarisation--------------    
elseif strcmp(sys.P, 'Radial')
    fprintf('Incident beam is radially polarised.\n');
    if strcmp(sys.plane, 'X-Y')
        fprintf('Calculation of the intensity distribution in the X-Y plane at z=%1.1f micron...\n', sys.z0*1e6);
        [Ix Iy Iz I] = IPSF_Vectorial_radial_xy(sys, X, Y);
    elseif strcmp(sys.plane, 'R-Z')
         fprintf('Calculation of the intensity distribution in the R-Z plane... \n');
        [Ixrz Iyrz Izrz Irz] = IPSF_Vectorial_radial_rz(sys, R, Z,0);
    end
    
%-------------Azimuthal polarisation--------------    
elseif strcmp(sys.P, 'Azimuthal')
    fprintf('Incident beam is azimuthally polarised.\n');
    if strcmp(sys.plane, 'X-Y')
        fprintf('Calculation of the intensity distribution in the X-Y plane at z=%1.1f micron...\n', sys.z0*1e6);
        [Ix Iy I] = IPSF_Vectorial_azimuthal_xy(sys, X, Y);
    elseif strcmp(sys.plane, 'R-Z')
         fprintf('Calculation of the intensity distribution in the R-Z plane... \n');
        [Ixrz Iyrz Irz] = IPSF_Vectorial_azimuthal_rz(sys, R, Z, 0);
    end
else
error('Could not identify the polarisation state.\n');   
end

%% Plot intensity distribution in the focal region
if strcmp(sys.plane,'X-Y')
    f=figure('NumberTitle','off','Name','Intensity in X-Y plane');
    plotintensitydistribution(sys, X, Y, I)
    xlabel('X(\lambda)')
    ylabel('Y(\lambda)')
    title('Intensity distribution in the X-Y plane')
    plotintensitycrosssectionxy(sys, X, Y, I)
elseif strcmp(sys.plane,'R-Z')
    f=figure('NumberTitle','off','Name','Intensity in R-Z plane');
    plotintensitydistribution(sys, R, Z, Irz)
    xlabel('R(\lambda)')
    ylabel('Z(\lambda)')
    title('Intensity distribution in the R-Z plane')
    plotintensitycrosssectionrz(sys, R, Z, Irz)
end