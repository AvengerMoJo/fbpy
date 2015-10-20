import fbpy.fb as fb
from fbpy.obj import Ddd
import numpy as np
import time

if __name__ == '__main__':

    main = fb.Surface()
    sub = fb.Surface((1,1),(270,270))
    sub.pixelstyle.color = fb.Color(10,40,10,0)
    sub.pixelstyle.style = fb.Styles.solid
    sub.pixelstyle.blur=1
    print "1"
    sfeer = Ddd('./raider2.obj',30)
    sfeer.open()
    print "2"
    spacecraft = fb.DDDObject(sfeer.x, sfeer.y, sfeer.z,sub)
    sub.dddtrafo.ex=-250
    sub.dddtrafo.ey=-250
    sub.dddtrafo.tetax=0.0
    sub.dddtrafo.tetay=0.0
    sub.dddtrafo.ez=155
    sub.dddtrafo.cz=400
    #camera
    print "3"

    for i in np.arange(0,6*np.pi,0.01):
        sub.dddtrafo.tetax = i*3
        sub.dddtrafo.ctetay = -(i)
        sub.dddtrafo.cx = -450*np.sin(i)
        sub.dddtrafo.cz = 450*np.cos(i)
        sub.dddtrafo.cy = 180
        sub.clear()
        spacecraft.draw()
        sub.update()
        #sub.grabsequence('/dev/shm/voyager')
        time.sleep(0.001)

