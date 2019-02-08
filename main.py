import cv2

def play_videoFile(filePath,mirror=False):

    cap = cv2.VideoCapture(filePath)
    cv2.namedWindow("Autonomous Video Croping",cv2.WINDOW_AUTOSIZE)
    while True:
        ret_val, frame = cap.read()

        if mirror:
            frame = cv2.flip(frame, 1)

        cv2.imshow("Autonomous Video Croping", frame)

        if cv2.waitKey(1) == ord('x'):
            break  # esc to quit

    cv2.destroyAllWindows()

def main():
    play_videoFile("output.avi",mirror=False)

if __name__ == "__main__":
    main()