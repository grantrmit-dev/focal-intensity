function plotintensitycrosssectionxy(sys, X, Y, I)% plot the intensity distribution along one dimension, 
    figure('NumberTitle','off','Name','Intensity along the X-direction');
    Imax=max(max(I));
    I = I./Imax; % Normalise I with the peak intensity in the focal region
    Ix = I(sys.re./2,:);
    plot(X./sys.wl,Ix,'k');
    xlabel('X(\lambda)')
    ylabel('Normalised I (A.U.)')
    title('Intensity distribution along the X-direction')
    figure('NumberTitle','off','Name','Intensity along the Y-direction');
    Iy = I(:,sys.re./2);
    plot(Y./sys.wl,Iy,'r');
    xlabel('Y(\lambda)')
    ylabel('Normalised I (A.U.)')
    title('Intensity distribution along the Y-direction')
end
    