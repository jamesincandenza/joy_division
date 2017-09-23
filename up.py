import pylab
import scipy

def gaussian(x, centre, xscale, height):
  return height * scipy.exp(-(2.*xscale*(x-centre))**2)

def triangle(x, centre, xscale, height):
  y = height * (1. - scipy.absolute(xscale*(x-centre)))
  return (y>0) * y

x = scipy.linspace(0., 1., 1501)
shape = triangle#gaussian#

def generate_noise(x, num_bumps, centre_min, centre_max, xscale_min, xscale_max, height_min, height_max, shape=shape):
  y = scipy.zeros_like(x)
  for i in xrange(num_bumps):
    centre = centre_min + (centre_max-centre_min)*scipy.rand()
    xscale = xscale_min + (xscale_max-xscale_min)*scipy.rand()
    height = height_min + (height_max-height_min)*scipy.rand()
    print(centre, xscale, height)
    y += shape(x, centre, xscale, height)
  return y

def generate_line(x):
  y = scipy.zeros_like(x)
  y += generate_noise(x, 100, 0., 1., 0., 300., 0., .003)
  y += generate_noise(x, 10, .25, .75, 20., 30., 0., .03)
  y += generate_noise(x, 10, .29, .45, 20., 30., 0., .03)
  return y

num_lines = 85
line_gap = .015
for i in xrange(num_lines):
  base_line = (num_lines-i)*line_gap
  y = base_line + generate_line(x)
  poly = pylab.Polygon([(x[0], base_line)]+zip(x, y)+[(x[-1], base_line)], facecolor='k', edgecolor='none', zorder=i)
  pylab.gca().add_patch(poly)
  pylab.plot(x, y, 'w', linewidth=2, zorder=i+.5)
pylab.gcf().patch.set_facecolor('black')
pylab.gca().set_axis_bgcolor('k')
pylab.axis('equal')
pylab.gcf().set_size_inches(8., 8.)
pylab.savefig('pulsar.png', facecolor=pylab.gcf().get_facecolor(), edgecolor='none', dpi=150)