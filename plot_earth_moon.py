#!/usr/bin/env python3

from matplotlib import pyplot as plt
from plot_common import (
    EARTH_RADIUS,
    MOON_RADIUS,
    COLOR_EARTH,
    COLOR_MOON,
    COLOR_MOON_ORBIT,
    COLOR_SC_ORBIT,
    Plot,
)


class PlotFreeReturn(Plot):
    def data_prepare(self):
        self.data_prepared = (
            self.data_raw['earth_pos'][0][:int(self.config['point_plotted'])],
            self.data_raw['earth_pos'][1][:int(self.config['point_plotted'])],
            self.data_raw['moon_pos'][0][:int(self.config['point_plotted'])],
            self.data_raw['moon_pos'][1][:int(self.config['point_plotted'])],
            self.data_raw['sc_pos'][0][:int(self.config['point_plotted'])],
            self.data_raw['sc_pos'][1][:int(self.config['point_plotted'])],
        )

        print('plot %d/%d points' % (self.config['point_plotted'], len(self.data_raw['earth_pos'][0])))

    def plot(self):
        ax = self.ax
        earth_xs, earth_ys, moon_xs, moon_ys, sc_xs, sc_ys = self.data_prepared

        # orbit: sc initial
        # ax.add_artist(plt.Circle((earth_xs[0], earth_ys[0]), EARTH_RADIUS+185*1000, edgecolor=COLOR_ORBIT_LEO, facecolor='none'))

        # earth and moon bodies
        ax.add_artist(plt.Circle((earth_xs[0], earth_ys[0]), EARTH_RADIUS, color=COLOR_EARTH))
        ax.add_artist(plt.Circle((moon_xs[0], moon_ys[0]), MOON_RADIUS, color=COLOR_MOON))

        # trajectories
        # plt.plot(earth_xs, earth_ys, '-', color=COLOR_EARTH_ORBIT)
        if self.config['show_moon_orbit']:
            plt.plot(moon_xs, moon_ys, '-', color=COLOR_MOON_ORBIT)
        plt.plot(sc_xs, sc_ys,  color = self.config['color'], label = self.config['param'])
        plt.grid(True)

# THRUST
#style = 'r--'
colorLine = 1
colorName = ['red','blue','yellow','green','purple','black','orange','green','aqua','brown','peru','pink','navy','seagreen','tan','darkgreen']
simDay = 13/2
for deltaV in range(3140, 3165, 3):
    angle = -123.7
    baseFile = 'deltav\\out_' + str(angle) + '_' + str(deltaV) + '.0'
    inFile = baseFile + '.txt'
    outFile = baseFile + '.svg'
    parValue = 'ΔV = ' + str(deltaV) + ' α = ' + str(angle)
    conf = {
        'xlim': (-40*10**6, 450*10**6),
        'ylim': (-390*10**6, 400*10**6),
        'infile': inFile,
        'outfile': outFile,
        'point_plotted': simDay * 86400/50,
        'show_moon_orbit': True,
        'param': parValue,
		'color': colorName[colorLine]
    }
    p = PlotFreeReturn (conf)
    p.go()
    colorLine = colorLine + 1
p.display('Free Return Trajectory for different thrust ΔV')

# ANGLE
colorLine = 1
for angle in range(110, 124, 3):
    deltaV = 3150
    baseFile = 'angle\\out_-' + str(angle) + '.7_' + str(deltaV) + '.0'
    inFile = baseFile + '.txt'
    outFile = baseFile + '.svg'
    parValue = 'ΔV = ' + str(deltaV) + ' α = ' + str(angle) + '.7'	
    conf = {
        'xlim': (-40*10**6, 450*10**6),
        'ylim': (-390*10**6, 400*10**6),
        'infile': inFile,
        'outfile': outFile,
        'point_plotted': simDay * 86400/50,
        'show_moon_orbit': True,
        'param': parValue,
        'color': colorName[colorLine]
    }
    p = PlotFreeReturn (conf)
    p.go()
    colorLine = colorLine + 1
p.display('Free Return Trajectory for different angle α')


'''
PlotFreeReturn({
    'xlim': (-150*10**6, 410*10**6),
    'ylim': (-20*10**6, 400*10**6),
    #'infile': 'data-free-return-with-moon-fixed.txt',
    'infile': 'out.txt',
    'outfile': 'freeReturn-scOrbitWithMoonFixed.svg',
    'point_plotted': 7.5 * 86400/50,
    'show_moon_orbit': True,
}).go()

# Calculating the trajectory - output
PlotFreeReturn({
    'xlim': (-35*10**6, 415*10**6),
    'ylim': (-30*10**6, 310*10**6),
    #'infile': 'data-free-return-with-moon-fixed.txt',
    'infile': 'out.txt',
    'outfile': 'calc-scOrbitWithMoonFixed.svg',
    'point_plotted': 7.5 * 86400/50,
    'show_moon_orbit': True,
}).go()
PlotFreeReturn({
    'xlim': (-35*10**6, 415*10**6),
    'ylim': (-170*10**6, 170*10**6),
    #'infile': 'data-free-return-with-moon-rotating.txt',
    'infile': 'out.txt',
    'outfile': 'calc-scOrbitWithMoonRotating.svg',
    'point_plotted': 7.5 * 86400/50,
    'show_moon_orbit': False,
}).go()
'''
