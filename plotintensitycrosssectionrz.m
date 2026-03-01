function plotintensitycrosssectionrz(sys, R, Z, I)% plot the intensity distribution along one dimension, 
    figure('NumberTitle','off','Name','Intensity along the R-direction');
    Imax=max(max(I));
    I = I./Imax; % Normalise I with the peak intensity in the focal region
    Ir = I(sys.re./2,:);
    plot(R./sys.wl,Ir,'k');
    xlabel('R(\lambda)')
    ylabel('Normalised I (A.U.)')
    title('Intensity distribution along the R-direction')
    figure('NumberTitle','off','Name','Intensity along the Z-direction');
    Iz = I(:,sys.re./2);
    plot(Z./sys.wl,Iz,'r');
    xlabel('Z(\lambda)')
    ylabel('Normalised I (A.U.)')
    title('Intensity distribution along the Z-direction')
end
    