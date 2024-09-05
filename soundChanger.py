from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import time
from random import randint

def soundChanger():
    try:
        devices = AudioUtilities.GetSpeakers()
        if not devices:
            print("No audio devices found.")
            return
        
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        if randint(0, 1) == 1:
            volume.SetMasterVolumeLevelScalar(0.0, None)
            print("Volume set to 0.0")
        else:
            volume.SetMasterVolumeLevelScalar(1.0, None)
            print("Volume set to 1.0")
    except Exception as e:
        print(f"An error occurred: {e}")

