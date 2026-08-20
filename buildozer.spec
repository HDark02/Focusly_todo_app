[app]

title = Focusly

package.name = focusly
package.domain = org.alexdynamo

source.dir = .

source.include_exts = py,kv,png,jpg,jpeg,json,ttf,atlas

version = 0.1

requirements = python3,kivy==2.1.0,kivymd==1.1.1

presplash.filename = app_icon.png

icon.filename = app_icon.png

orientation = portrait

fullscreen = 0

android.presplash_color = black

# Aucune permission Internet
# Aucune permission de stockage externe

android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a

android.allow_backup = True


[buildozer]

log_level = 2
warn_on_root = 1
