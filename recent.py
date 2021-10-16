import os
import cv2
import pytesseract
import re
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#READ IMAGE FOR LEVEL AND CLEAR TYPE
def read_img(name):
    #OPEN IMAGE AND CONVERT TO BLACK AND WHITE
    img = cv2.imread(name, 0)
    thresh = 255 - cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    #GET LEVEL
    x,y,w,h = 1185, 685, 95, 35  
    level = pytesseract.image_to_string(img[y:y+h,x:x+w])

    if level[0] == "a":
        level = pytesseract.image_to_string(thresh[y:y+h,x:x+w])

    #GET CLEAR TYPE
    x,y,w,h = 286, 233, 87, 25
    clear = pytesseract.image_to_string(img[y:y+h,x:x+w])

    return level, clear

#PROCESS IMAGES, SEPARATE LEVEL AND CLEAR TYPE TO FILE
def process():
    out = 'RECENT\n'
    files = os.listdir(".")

    for i in os.listdir(".")[::-1]:
        if i.endswith(".png") and i.startswith("LR2"):
            read = read_img(os.path.join(".",i))
            level = read[0][:-2]
            clear = read[1][:-2]
            
            #SP FORMATING
            if level[0:2] == "SP":
                level = re.findall(r"\D+(\d+)",level)
                level = "SP" + level[0]
            
            #O -> 0
            if level == "stO":
                level = "st0"

            if level == "slO":
                level = "sl0"

            
            #OUTPUT: SP20 HC
            out += level
            if clear == "CLEAR":
                out += " NC\n"
            elif "COMBO" in clear:
                out += " FC\n"
            else:
                out += " HC\n"

    #TO FILE            
    text = open("recent.txt","w+")
    text.write(out)
    text.close()    


#WATCH DIRECTORY FOR NEW IMAGES
def watch():
    patterns = ["*.png"]
    ignore_patterns = None
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_created(event):
        time.sleep(3)
        process()

    def on_deleted(event):
        time.sleep(3)
        process()

    #def on_modified(event):
    #    process()

    #def on_moved(event):
    #    process()

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    #my_event_handler.on_modified = on_modified
    #my_event_handler.on_moved = on_moved

    path = "."
    go_recursively = False
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()


if __name__ == "__main__":
    process()
    watch()

    

    
