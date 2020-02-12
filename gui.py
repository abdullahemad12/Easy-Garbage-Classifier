import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import classify

model = classify.load_model()
root = tkinter.Tk()
root.geometry("{0}x{1}+0+0".format(
            root.winfo_screenwidth(), root.winfo_screenheight()))

def stop_capture():
    bStart["text"] = "Start Capture"
    bStart["command"] = start_capture
    bSnap.pack_forget()
    cap.release()

def update():
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            root.photo = photo
            root.dispPhoto = videoCanv.create_image(0, 0, image=root.photo, anchor=tkinter.NW)
        root.after(15, update)
    else:
        videoCanv.delete(root.dispPhoto)

def start_capture():
    bStart["text"] = "Stop Capture"
    bStart["command"] = stop_capture
    bSnap.pack()
    global cap
    cap = cv2.VideoCapture(0)
    ret = cap.set(3,vid_width)
    ret = cap.set(4,vid_height)
    update()

def classify_snap(img):

    img = cv2.resize(img, dsize=(300, 300), interpolation=cv2.INTER_CUBIC)
    img = img.reshape(1, img.shape[0],img.shape[1], img.shape[2])
    img = img / 255.0;
    className = classify.predict(model, img)
    classLabel["text"] = className

def take_snapshot():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        root.snap = photo
        snapCanv.create_image(0, 0, image=root.snap, anchor=tkinter.NW)
        classify_snap(frame)


tkinter.Label(root, text="Press Button to Start Video Capture!").pack()
vid_width = 320
vid_height = 240

videoCanv = tkinter.Canvas(root, width=vid_width, height=vid_height)
videoCanv.pack()

bStart = tkinter.Button(root, text="Start Capture", width=25, command=start_capture)
bStart.pack()
bSnap = tkinter.Button(root, text="Take Snapshot", width=25, command=take_snapshot)

tkinter.Label(root, text="Classification:").pack()

classLabel = tkinter.Label(root, text="No snapshots to classify yet.")
classLabel.pack()

snapCanv = tkinter.Canvas(root, width=vid_width, height=vid_height)
snapCanv.pack()

root.mainloop()
