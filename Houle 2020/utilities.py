from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime

def plot(timeSnapShot,arrayElectric,arrayMagnetic):
        # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("date_%d_%m_%Y_time_%H_%M_%S_timeSnapShot_"+str(timeSnapShot))
    print("date and time =", dt_string)	
    ondimensional = arrayElectric[:,timeSnapShot]
    
    plt.rcParams['font.size'] = 12
    plt.figure(figsize=(8, 3.5))
    
    plt.subplot(211)
    plt.plot(arrayElectric[:,timeSnapShot], color='k', linewidth=1)
    plt.ylabel('E$_x$', fontsize='14')
    plt.xticks(np.arange(0, ondimensional.size + 1, step=20))
    plt.xlim(0, ondimensional.size)
    plt.yticks(np.arange(-1, 1.2, step=1))
    plt.ylim(-1.2, 1.2)
    plt.text(100, 0.5, 'T = {}'.format(timeSnapShot),horizontalalignment='center')

    plt.subplot(212)
    plt.plot(arrayMagnetic[:,timeSnapShot], color='k', linewidth=1)
    plt.ylabel('H$_y$', fontsize='14')
    plt.xlabel('FDTD cells')
    plt.xticks(np.arange(0, ondimensional.size + 1, step=20))
    plt.xlim(0, ondimensional.size)
    plt.yticks(np.arange(-1, 1.2, step=1))
    plt.ylim(-1.2, 1.2)
    plt.subplots_adjust(bottom=0.2, hspace=0.45)
    # plt.show()
    plt.savefig(dt_string)