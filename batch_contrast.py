import cv2
import os

def interpolate_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))*4
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))*4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Resize the frame to the desired dimensions
        resized_frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_LINEAR)
        # Increase the contrast of the frame
        ret, thresh = cv2.threshold(resized_frame, 240, 255, cv2.THRESH_TOZERO)
        # Write the adjusted frame to the output video
        out.write(thresh)

# Example usage
input_dir = r"D:\Tierpsy_analysis\Rhomboid_FINALE\processed\rom-2\WF"
output_dir = r"D:\Tierpsy_analysis\Rhomboid_FINALE\interpolated"
for filename in os.listdir(input_dir):
    if filename.endswith(".avi"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        print(filename +" being processed!")
        interpolate_video(input_path, output_path)
        print("done!")