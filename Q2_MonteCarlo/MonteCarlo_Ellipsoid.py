import random
import matplotlib.pyplot as plt


def f(x, y, z, a, b, c):                            ##function for ellipsoid
    return x**2/a**2 + y**2/b**2 + z**2/c**2

def vol_ellipsoid(a, b, c, N):                      ##function for volume of ellipsoid in montecarlo method
    sum = 0
    X, Y, Z = [], [], []
    for i in range(N):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
        z = random.uniform(-c, c)
        if f(x,y,z,a,b,c) <= 1:
            X.append(x)
            Y.append(y)
            Z.append(z)
            sum += 1
        vol = (sum/N)*8*a*b*c
    return vol, X, Y, Z                             ##returning volume and X,Y,Z list to generate ellipsoid in later question


N_list, vol_List, error_list= [], [], []            ##generating required lists for plotting

for i in range(1, 496, 5):                          ##question a
    N = i*100
    N_list.append(N)                                ##list of N
    v, x, y, z = vol_ellipsoid(1, 1.5, 2, N)
    vol_List.append(v)
    error_list.append(abs(v - 12.57) / v)           ##12.57 is the analytical solution of volume


#############  plotting for quation (b)

plt.axhline(y=12.57, color="red", label='Analytical value (12.57 unit^3)')  ##12.57 is the analytical solution of volume
plt.plot(N_list,vol_List, 'bx', label='computed value (Montecarlo)')
plt.plot(N_list,vol_List)

plt.title('comparison between analytical and numerical value')
plt.xlabel('N')
plt.ylabel('Volume of Ellipsoid')
plt.legend(shadow=True)
plt.grid()

plt.savefig('2.(b)comparison.pdf')
plt.show()


#############  plotting for quation (c)

plt.scatter(N_list,error_list)
plt.plot(N_list,error_list)

plt.title('Fractional Error vs Step Number graph')
plt.xlabel('Step Number')
plt.ylabel('Fractional error')
plt.grid()

plt.savefig('2.(c)fractional error graph.pdf')
plt.show()


#############  plotting for quation (d)

v,x,y,z = vol_ellipsoid(1, 1.5, 2, 25000)
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z, c=z);
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Projection of Ellipsoid')
plt.savefig('2.(d)projection.pdf')
plt.show()


