from __future__ import division, print_function
import time, math

def turn_left(lbot, duration=0, rotSpeed=-0.2, verbose=False):
	lbot.setRobotSpeed(lbot.adv, rotSpeed)
	if verbose:
		print('~ Learnbot turning left ...')
	if duration != 0:
		time.sleep(duration)

