# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
print "install apk"

device.installPackage('/data/android-project/camtenzo/app/build/outputs/apk/app-release.apk')

# sets a variable with the package's internal name
package = 'com.katenzo.camtenzo'

# sets a variable with the name of an Activity in the package
activity = 'com.katenzo.camtenzo.CameraActivity'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
print "Start Camera Activity"
device.startActivity(component=runComponent)

MonkeyRunner.sleep(3)
print "Take Snapshot Camera"
screen = device.takeSnapshot()
screen.writeToFile('screen/camera.png','png')
MonkeyRunner.sleep(3)
print "Press Home Button"
# Presses the Menu button
device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)

# Takes a screenshot
print "Take Snapshot Home";

result = device.takeSnapshot()

# Writes the screenshot to a file
result.writeToFile('screen/main.png','png')
