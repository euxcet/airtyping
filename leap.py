import sys
if (sys.platform == "darwin"):
	import osx.Leap as Leap
	from osx.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
elif (sys.platform == "win32"):
	import windows.Leap as Leap
	from windows.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
