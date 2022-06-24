import cv2, time
from os import mkdir

# ===============================================================
try:
    mkdir('Saved Video')
except FileExistsError:
    pass


# = Video Camera=
def camera():
    video = cv2.VideoCapture(0)

    video.set(3, 500)
    video.set(4, 600)

    print("Press q to exit the Video")
    # ==========
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    date_time = time.strftime("Camera Recorded on %d-%m-%Y at %H-%M-%p")  # set current time as video name
    output = cv2.VideoWriter('Saved Video/' + date_time + '.mp4', fourcc, 20.0, (500, 400))
    # =====
    while video.isOpened():
        check, frame = video.read()
        if check == True:
            frame = cv2.flip(frame, 1)

            # show time of recording

            t = time.ctime()

            cv2.putText(frame, t, (0, 20),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (5, 5, 5), 1)

            cv2.imshow('Video', frame)
            output.write(frame)

            # Close window when user click esc button
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Your Video Is Saved In Current Directory.")
                break


        else:
            print("Cannot open this camera. Check its configuration.")
            break
    video.release()
    output.release()
    cv2.destroyAllWindows()


# ================================= now time to run the app==================

ask = int(input('Do you want to Start your Video?\nEnter 1 for Yes\nEnter 2 for No\n>>> '))
if ask == 1:
    camera()
elif ask == 2:
    print("Have A Wonderful Day!")
    exit
