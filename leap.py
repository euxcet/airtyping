import sys
if (sys.platform == "darwin"):
	import osx.Leap as Leap
	from osx.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
