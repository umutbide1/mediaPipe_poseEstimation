import cv2
import mediapipe as mp
import os

# MediaPipe Pose modülü ve çizim araçları
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# İşlenecek video dosyalarının bulunduğu dizin ve isimleri
video_folder = "./"  # Bu kodun bulunduğu dizin
video_files = ["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4"]

# MediaPipe Pose modelini tanımlama
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    enable_segmentation=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

