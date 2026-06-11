import cv2
from ultralytics import YOLO
import math


# --- AYARLAR ---
# 1. Colab'dan indirdiğin dosyanın adı (Aynı klasörde olsunlar)
model_path = "best.pt"

# 2. Modeli yükle
model = YOLO(model_path)

# 3. Sansürlenecek sınıfların tam isimleri (Roboflow'dakiyle birebir aynı olmalı)
sansurlenecekler = ["nah", "orta_parmak", "kapak"]

# Kamerayı başlat
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Genişlik
cap.set(4, 720)  # Yükseklik

print("Kamera başlatıldı. Çıkmak için 'q' tuşuna basınız.")

CONFIDENCE_THRESHOLD = 0.4

while True:
    success, img = cap.read()
    if not success: break

    img = cv2.flip(img, 1)

    # Model tahmini
    results = model(img, stream=True, verbose=False, conf=CONFIDENCE_THRESHOLD)

    detected_dangerous = False  # Bu karede tehlikeli hareket var mı?

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            currentClass = model.names[cls_id]

            # Koordinatları al
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Sınır kontrolü
            h, w, _ = img.shape
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(w, x2), min(h, y2)

            if currentClass in sansurlenecekler:
                # SANSÜRLEME
                roi = img[y1:y2, x1:x2]
                if roi.size > 0:
                    # Bulanıklığı artırdım (daha güçlü sansür)
                    img[y1:y2, x1:x2] = cv2.GaussianBlur(roi, (99, 99), 50)

                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(img, "SANSUR", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            elif currentClass == "normal_el":
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, "Normal", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Proje", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()