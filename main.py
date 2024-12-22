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

# Her video üzerinde döngü ile işlem yap
for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)
    cap = cv2.VideoCapture(video_path)

    # Video özelliklerini al
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_path = f"processed_{video_file}"
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    print(f"İşleniyor: {video_file}")
    while True:
        success, frame = cap.read()
        if not success:
            break

        # İşlenecek video üzerinde poz tespiti
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # Eğer pose tespiti yapılmışsa çizim yap
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
            )

        # İşlenmiş kareyi kaydet ve göster
        out.write(frame)
        cv2.imshow(f"Processing {video_file}", frame)

        # ESC ile çıkış
        if cv2.waitKey(1) & 0xFF == 27:
            print(f"Videodan erken çıkıldı: {video_file}")
            break

    cap.release()
    out.release()
    cv2.destroyWindow(f"Processing {video_file}")
    print(f"{output_path} kaydedildi.")

