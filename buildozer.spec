[app]
# (str) Title of your application
title = JARVIS PRO

# (str) Package name
package.name = jarvis_ram

# (str) Package domain (needed for android packaging)
package.domain = org.ram

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,mp3

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Yahan humne saari libraries daal di hain
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,google-generativeai,gTTS,SpeechRecognition,urllib3,requests,certifi,idna

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
# WhatsApp aur Voice ke liye permissions
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use (33 is for latest Android)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The Android arch to build for
android.archs = armeabi-v7a, arm64-v8a

# (bool) Allow backup of data
android.allow_backup = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifacts
bin_dir = ./bin
