[app]

# (str) Title of your application
title = Jarvis AI

# (str) Package name
package.name = jarvis_ai

# (str) Package domain (needed for android packaging)
package.domain = org.rambhuyan

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Ismein aapki saari libraries add kar di gayi hain
requirements = python3, kivy==2.2.1, kivymd==1.1.1, google-generativeai, gTTS, SpeechRecognition, Pillow, requests, charset-normalizer, idna, urllib3, certifi

# (str) Custom source folders for requirements
# (list) Permissions
# Jarvis ke liye Mic aur Internet zaroori hai
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) List of service to declare
services = 

# (str) Path to a custom whitelist file
# android.whitelist =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

