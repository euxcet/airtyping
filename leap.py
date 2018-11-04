import sys
if (sys.platform == "darwin"):
	import lib.Leap as Leap
	from lib.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
elif (sys.platform == "win32"):
	import windows.Leap as Leap
	from windows.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
