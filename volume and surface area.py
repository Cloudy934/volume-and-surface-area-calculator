from math import *
shapes = dict()
shapes['cone'] = ''
shapes['cube'] = ''
shapes['cylinder'] = ''
shapes['rectangular prism'] = ''
shapes['pyramid'] = ''
shapes['sphere'] = ''
shapes['hemisphere'] = ''
shapes['frustrum'] = ''
shapes['torus'] = ''
shapes['ellipsoid'] = ''
shapes['octahedron'] = ''
shapes['rhombicosidodecahedron'] = ''
shapes['dodecahedron'] = ''
shapes['icosahedron'] = ''
shapes['hexagonalpyramid'] = ''
shapes['hexagonalprism'] = ''
shapes['pentagonalprism'] = ''
shapes['pentagonalpyramid'] = ''
shapes['octagonalprism'] = ''
shapes['triangularprism'] = ''
shapes['tetrahedron'] = ''
shapes['paraboloid'] = ''
shapes['hyperboloid'] = ''
shapes['prolatespheroid'] = ''

while True:    
        try:
            shape = input("Insert the name of a 3D figure to find its surface area and volume: ").replace(' ','')
        except ValueError:
            print("Invalid input")
            continue
        if shape == '?':
            print("Insert one of the following figures:")
            for key, value in shapes.items():
                print(key)
        elif shape.lower() not in shapes:
            print("Unregistered Figure. Enter one of the following shapes:")
            for key, value in shapes.items() :
                print(key)
            continue
        if shape == 'whats a 3D figure':
            print("a 3D figure is a shape for example a cube or a cylinder it's a 3D shape")
        else:
            break
if shape.lower() == 'cone':
    h = float(input("What is the height of the cone? "))
    r = float(input("What is the radius of the cone? "))
    volume = (1/3 * pi * r**2 * h)
    surface_area = (pi * r * (r + sqrt(h**2 + r**2)))
    print("Volume:", round(volume, 2), 'or', round((volume/pi), 2), 'pi')
    print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'cube':
    s = float(input("What is the length of one side of the cube? "))
    volume = (s**3)
    surface_area = (6* s**2)
    print("Volume:", round(volume, 2))
    print("Surface Area:", round(surface_area, 2))

if shape.lower() == 'cylinder':
    h = float(input("What is the height of the cylinder? "))
    r = float(input("What is the radius of the cylinder? "))
    volume = (pi * r**2 * h)
    surface_area = (2 * pi * r * h + 2 * pi * r**2)
    print("Volume:", round(volume, 2), 'or', round((volume/pi), 2), 'pi')
    print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'rectangular prism':
    l = float(input("What is the length of the prism? "))
    w = float(input("What is the width of the prism? "))
    h = float(input("What is the height of the prism? "))
    volume = (l * w * h)
    surface_area = (2 * l * w + 2 * (l + w) * h)
    print("Volume:", round(volume, 2))
    print("Surface Area:", round(surface_area, 2))    

if shape.lower() == 'pyramid':
    l = float(input("What is the length of the pyramid's base? "))
    w = float(input("What is the width of the pyramid's base? "))
    h = float(input("What is the height of the pyramid? "))
    volume = (l * w * h / 3)
    surface_area = ((l * w) + l * sqrt((w/2)**2 +h**2) + w * sqrt((l/2)**2 + h**2))
    print("Volume:", round(volume, 2))
    print("Surface Area:", round(surface_area, 2))

if shape.lower() == 'sphere':
    r = float(input("What is the radius of the sphere? "))
    volume = (4 * pi * r**3 / 3)
    surface_area = (4 * pi * r**2)
    print("Volume:", round(volume, 2), 'or', round((volume/pi), 2), 'pi')
    print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')
    
if shape.lower() == 'hemisphere':
    r = float(input("What is the radius of the hemisphere? "))
    volume = (2 * pi * r**3 / 3)
    surface_area = (3 * pi * r**2)
    print("Volume:", round(volume, 2), 'or', round((volume/pi), 2), 'pi')
    print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')
    
if shape.lower() == 'frustrum':
    r = float(input("What is the radius of the top of the frustrum? "))
    R = float(input("What is the radius of the bottom of the frustrum? "))
    h = float(input("What is the height of the frustrum? "))
    volume = ((pi/ 3) * h * (R**2 + r**2 + R * r))
    root_this = ((R-r)**2+h**2)
    surface_area = (pi * (R + r) * sqrt(root_this) + pi*(R**2) + pi*(r**2))
    print("Volume:", round(volume, 2), 'or', round((volume/pi), 2), 'pi')
    print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'torus':
        r = float(input("What is the major radius of your torus?"))
        R = float(input("What is the minor radius of your torus?"))
        volume = ((pi * r**2) * (2 * pi * R))
        surface_area = (4 * pi**2 * R * r)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')
        
if shape.lower() == 'ellipsoid':
        a = float(input("What is the a axis of your ellipsoid?"))
        b = float(input("What is the b axis of your ellipsoid?"))
        c = float(input("What is the c axis of your ellipsoid?"))
        volume = (4/3 * pi * a * b * c)
        surface_area = (4 * pi * ((a * b)**1.6 + (a * c)**1.6 + (b * c)**1.6 / 3)**1/1.6)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'octahedron': 
        a = float(input("What is the edge of your octahedron?"))
        volume = (sqrt(2)/3 * a**3)
        surface_area = (2 * sqrt(3)* a**2)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'rhombicosidodecahedron':
        a = float(input("What is the edge length of your Rhombicosidodecahedron?"))
        volume = (2/3 * a**3 * (6 + 5 * sqrt(2)))
        surface_area = (2 * a**2 * (9 + sqrt(3)))
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'dodecahedron':
        a = float(input("What is the edge length of your dodecahedron?"))
        volume = ( (15 + 7 * sqrt(5)) * a**3)
        surface_area = (3 * sqrt(25 + 10) * sqrt(5) * a**2)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')                

if shape.lower() == 'icosahedron':
        a = float(input("What is the edge length of your icosahedron"))
        volume = (5 * (3 + sqrt(5)) /12 * a**3)
        surface_area = (5 * sqrt(3) * a**2)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'hexagonalpyramid':
        a = float(input("What is the base edge length of your hexagonal pyramid?"))
        h = float(input("What is the height of your hexagonal pyramid?"))
        volume = (sqrt(3)/2 * a**2 * h)
        surface_area = ((3 * sqrt(3) / 2) * a**2 + 3 * a * sqrt(h**2 + 3*a**2/4))
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')
        
if shape.lower() == 'hexagonalprism':
        a = float(input("What is the base edge length of your prism?"))
        h = float(input("What is the height of oyur prism?"))
        volume = ( (3 * sqrt(3))/2 * a**2 * h)
        surface_area = (6 * a * h + 3 * sqrt(3) * a**2)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'pentagonalprism':
        a = float(input("What is the base edge length of your prism"))
        h = float(input("What is the height of your prism"))
        volume = ( 1/4 * (sqrt(5(5 + 2 * sqrt(5))) * a**2 * h))
        surface_area = (5 * a * h + 1/2 * (sqrt(5(5 + 2 * sqrt(5)))) * a**2)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')       

if shape.lower() == 'pentagonalpyramid':
        a = float(input("What is the base edge length of your prism"))
        h = float(input("What is the height of your prism"))
        volume = (5/12 * tan(54) * h * a**2)
        surface_area = (5/4 * tan(54) * a**2 + 5 * a/2 * sqrt(h**2 + (a * tan(54)) /2 **2))
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'octagonalprism':
        a = float(input("What is the base edge length of your prism"))
        h = float(input("What is the height of your prism"))
        volume = ( 2 * (1 + sqrt(2)) * a**2 * h)
        surface_area = (8 * a * h + 4 * (1 + sqrt(2)) * a**2)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'triangularprism':
        a = float(input("What is the first base side of your prism?"))
        b = float(input("What is the second base side of your prism?"))
        c = float(input("What is the third base side of your prism?"))
        h = float(input("What is the height of your prism?"))
        volume = (1/4 * h * sqrt(-a**4 + 2 * (a * b)**2 * -b**4 + 2 * (b * c)**2 * -c**4))
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'tetrahedron':
        a = float(input("What is the edge length of your tetrahedron?"))
        volume = (a**3 / 6 * sqrt(2))
        surface_area = (sqrt(3) * a**2)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'paraboloid':
        r = float(input("What is the radius of your paraboloid?"))
        h = float(input("What is the height of your paraboloid?"))
        a = float(input("What is the input value of your paraboloid?"))
        volume = ((pi/2) * h * r**2)
        surface_area = (pi * a/ (6 * h**2) * (a**2 + 4 * h**2)**3/2 * -a**3)
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')
 
if shape.lower() == 'hyperboloid':
        r = float(input("What is the base radius of your hyperboloid?"))
        a = float(input("What is the skirt radius of your hyperboloid?"))
        h = float(input("What is the height of your hyperboloid?"))
        volume = (1/3 * pi * h * (2 * a**2 + r**2))
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        
if shape.lower() == 'prolatespheroid':
        a = float(input("What is the equatorial semi axes of your prolate spheroid?"))
        c = float(input("What is the polar semi axes for your prolate spheroid?"))
        volume = (4/3 * pi * a**2 * c)
        surface_area = (2 * pi * a * (a + c**2 / sqrt(a**2 - c**2 * arcsinh(sqrt(a**2 - c**2)))))
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'oblatespheroid':
        a = float(input("What is the equatorial semi axes of your prolate spheroid?"))
        c = float(input("What is the polar semi axes for your prolate spheroid?"))
        surface_area = (2 * pi * a * (a + c**2 / sqrt(a**2 - c**2 * arcsinh(sqrt(a**2 - c**2)))))
        print("volume:", round(volume, 2), 'or', round((volume/pi), 2) , 'pi')
        print("Surface Area:", round(surface_area, 2), 'or', round((surface_area/pi), 2), 'pi')
