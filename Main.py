import os
import shutil

dir = input("Enter the HL directory: ")
mName = input("Enter the mod name: ")

newPath = dir + "/" + mName

print(newPath)

liblistContent = """
// Valve Game Info file
//  These are key/value pairs.  Certain mods will use different settings.
//
game {}
startmap "c0a0"
trainmap "t0a0"
mpentity "info_player_deathmatch"
gamedll "dlls\hl.dll"
gamedll_linux "dlls/hl.so"
gamedll_osx "dlls/hl.dylib"
secure "1"
type "singleplayer_only"
animated_title "1"
hd_background "1"
""".format('"' + mName + '"')

summary = """
*-*-*-*-*-Summary*-*-*-*-*-

Half-Life path: {}
      
Mod name: {}
""".format(dir,mName)

print(summary)

con = input("Press Enter to start")

if not os.path.exists(newPath):
    os.makedirs(newPath)
    os.makedirs(newPath + "/cl_dlls")
    os.makedirs(newPath + "/maps")
    print("DIRS:Done!")
    liblist = open(newPath + "/liblist.gam","x")
    liblist.write(liblistContent)
    liblist.close()
    print("LIBLIST:Done!")
    shutil.copy(dir + "/valve/cl_dlls/client.dll",newPath + "/cl_dlls/client.dll")
    shutil.copy(dir + "/valve/cl_dlls/client.dylib",newPath + "/cl_dlls/client.dylib")
    shutil.copy(dir + "/valve/cl_dlls/client.so",newPath + "/cl_dlls/client.so")
    shutil.copy(dir + "/valve/cl_dlls/gameui.so",newPath + "/cl_dlls/gameui.so")
    shutil.copy(dir + "/valve/cl_dlls/particleman.so",newPath + "/cl_dlls/particleman.so")
    print("DLL/0S:Done!")
con2 = input("Done!,press Enter to exit!")
