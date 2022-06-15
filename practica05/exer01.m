function y = Laplace(ua,ub,uc,ud,n,m,h,error)
clear u;
for i=1:n+2
    u(i,1)=uc;
    u(i,m+2)=ud;
end

for j=1:m+2
    u(1,j)=ua;
    u(n+2,j)=ub;
end
p = (ua+ub+uc+ud)/4;
for i =2:n+1
    for j=2:m+1
        u(i,j)=p;
    end
end
k=0;
conv=0;

while k<h && conv ==0
    k = k+1;
    t=u;
    for i=2:n+1
        for j=2:m+1
            u(i,j)=0.25*(u(i+1,j)+u(i-1,j)+u(i,j+1)+u(i,j-1));
        end
    end
    if norm((u-t),inf)/norm(u,inf)<error
        conv=1;
    end
end

if conv==1
    disp(u)
    disp(k)
    [x,y]=meshgrid(1:m+2,1:n+2);
    surf(x,y,u)
    shading flat
else 
    disp('no converge')
end