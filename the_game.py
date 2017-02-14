import space as sl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import simple_animation as s_anim
import time


print 'Initializing space...'
space=sl.Space(100,200)
print '...done.\n'


print 'Running the game of life...'

t0=time.clock()

list_of_arrays=[]
for i in range(256):
	list_of_arrays.append(space.plane.copy())
	space.MakeStep()

t1=time.clock()
time_difference=t1-t0

print '...done in ', time_difference, ' seconds.\n'


print 'Creating animation'
anim=s_anim.SimpleAnimation(list_of_arrays)
anim.animate()
anim.save('myLife.mp4', 6)