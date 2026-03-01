function sys = systempra % Set system parameters, the unit is metre
sys.wl = 800e-9; % Free space wavelength of the laser beam
sys.re = 210; % Resolution in the image plane (number of pixels)
sys.r = 1e-6; % Calculation diameter in the image plane 
sys.z = 1e-6; % Calculation distance in the axial direction
sys.z0 = 0e-6; % Position of image plane
sys.NA = 1.4; % Numerical aperture of the objective
sys.n = 1.514; % Index of the immersion material 
               % For a water lens "n = 1.33"
               % For a air lens "n = 1"
sys.P = 'Circular';% Define the polarisation state of the incidence, which is case sensitive. 
                 % 'Linear' for linear polarisation
                 % 'Circular' for left-handed circular polarisation (LCP)
                 % 'Radial' for radial polarisation
                 % 'Azimuthal' for azimuthal polarisation
sys.e = 0; % Normalised radius of the annular aperture (from 0 to 1), "0" means a circular aperture
sys.m = 0; % Topological charge of the phase vortices("+" means left-handed phase vortices,
           % "-" meas right-handed phase vortices), "0" means a planewave
           % incident beam
sys.plane = 'R-Z';%'X-Y' for x-y plane calculation (case sensitive)
                  %'R-Z' for r-z plane calculaiton
end