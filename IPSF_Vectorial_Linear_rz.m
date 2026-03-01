function [Ex Ey Ez Ix Iy Iz I] = IPSF_Vectorial_Linear_rz(sys, R, Z,ang)
   [r z] = meshgrid(R,Z);
    n = sys.n;
    wl = sys.wl;
    NA = sys.NA;
    a = asin(NA/n);
    k = (2*pi)/wl;
    m = sys.m;
    e = sys.e;
    Tho = NA/n;
    th1 = asin(e.*Tho);
    
    I0 = quadv(@E0field,th1,a);
    I2 = quadv(@E2field,th1,a);
    I3 = quadv(@E3field,th1,a);
    I4 = quadv(@E4field,th1,a);
    I5 = quadv(@E5field,th1,a);
    
     
    Ix = abs(((1i).^m.*exp(1i.*m.*ang).*I0-.5.*(((1i).^(m+2).*exp(1i.*(m+2).*ang).*I2+(1i).^(m-2).*exp(1i.*(m-2).*ang).*I3))).^2);
    Iy = abs((0.5.*(-(1i).^(m+2).*exp(1i.*(m+2).*ang).*I2+(1i).^(m-2).*exp(1i.*(m-2).*ang).*I3)).^2);
    Iz = abs((((1i).^(m+1).*exp(1i.*(m+1).*ang).*I4+(1i).^(m-1).*exp(1i.*(m-1).*ang).*I5)).^2);
    Ex = abs(((1i).^m.*exp(1i.*m.*ang).*I0-.5.*(((1i).^(m+2).*exp(1i.*(m+2).*ang).*I2+(1i).^(m-2).*exp(1i.*(m-2).*ang).*I3))));
    Ey = abs(0.5.*(-(1i).^(m+2).*exp(1i.*(m+2).*ang).*I2+(1i).^(m-2).*exp(1i.*(m-2).*ang).*I3));
    Ez = abs(((1i).^(m+1).*exp(1i.*(m+1).*ang).*I4+(1i).^(m-1).*exp(1i.*(m-1).*ang).*I5));
    I=Ix+Iy+Iz;
    function E0 = E0field(th)
       Pr = 1;
       E0 = Pr.*(cos(th).^(1/2)).* sin(th).*(1+cos(th)).* besselj(m,k.*r.*n.* sin(th)).*exp(-1i.*k.*z.*n.*cos(th));
    end

    function E2 = E2field(th)
        Pr = 1;
        E2 = Pr.*(cos(th).^(1/2)).* sin(th).*(1-cos(th)).*besselj(m+2, k .* r .* n .* sin(th)).*exp(-1i.*k.*z.*n.*cos(th));
    end

    function E3 = E3field(th)
        Pr = 1;
        E3 = Pr.*(cos(th).^(1/2)).* sin(th).*(1-cos(th)).* besselj(m-2, k .* r .* n .* sin(th)).*exp(-1i.*k.*z.*n.*cos(th));
    end
 function E4 = E4field(th)
        Pr = 1;
        E4 = Pr.*(cos(th).^(1/2)).* (sin(th).^2).*besselj(m+1, k .* r .* n .* sin(th)).*exp(-1i.*k.*z.* n .* cos(th));
 end

 function E5 = E5field(th)
        Pr = 1;
        E5 = Pr.*(cos(th).^(1/2)).* (sin(th).^2).*besselj(m-1, k .* r .* n .* sin(th)).*exp(-1i.*k.*z.*n.*cos(th));
    end
end