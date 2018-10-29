import sys
if (sys.platform == "darwin"):
	import lib.Leap as Leap
	from lib.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
