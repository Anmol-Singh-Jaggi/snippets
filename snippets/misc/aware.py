from win10toast import ToastNotifier
import time


toaster = ToastNotifier()
while True:
    toaster.show_toast("!!!!!", "#####")
    time.sleep(25*60)