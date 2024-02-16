#!/bin/bash

if [ -z "$ANDROID_SERIAL" ]; then
  export ANDROID_SERIAL=emulator-5554
fi
crosscore='/sdcard/Android/data/com.megagame.crosscore/files'

adb push Android/videos $crosscore
adb push Android/Custom $crosscore
adb push Android/internation.txt $crosscore
user=$(adb shell "stat -c '%U' $crosscore")
group=$(adb shell "stat -c '%G' $crosscore")
adb shell chown -R $user:$group $crosscore
adb shell chmod -R g+w $crosscore
