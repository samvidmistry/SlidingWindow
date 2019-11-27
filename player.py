import sys
import cv2

def start_slideshow(video_file_path: str, timing_file_path: str):
    cap = cv2.VideoCapture(video_file_path)
    cv2.namedWindow(video_file_path, cv2.WINDOW_GUI_EXPANDED)
    cv2.setWindowProperty(video_file_path, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    fps = cap.get(cv2.CAP_PROP_FPS)
    with open("timings.txt", 'r') as times:
        run_times = list(map(float, times.readlines()))

    pointer = 0
    current_frame = run_times[pointer] * fps
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    pointer += 1

    while pointer < len(run_times):
        while current_frame < (run_times[pointer] * fps):
            ret_val, frame = cap.read()
            current_frame += 1
            cv2.imshow(video_file_path, frame)

            if cv2.waitKey(1) == 27:
                break
        current_frame = run_times[pointer] * fps
        pointer += 1

    cv2.destroyAllWindows()

def main():
    if len(sys.argv) < 3:
        print("Please provide path of video file as first argument and timing file as second argument")
        exit(0)
    
    start_slideshow(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
