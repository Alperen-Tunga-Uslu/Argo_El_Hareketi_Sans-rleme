# 🛡️ Görüntü Sansürleme Uygulaması (Python, YOLOv8, Roboflow)

Bu proje; görüntülerdeki hassas içerikleri nesne tespiti (object detection) yöntemiyle otomatik olarak tespit eden ve bu bölgeleri dinamik olarak sansürleyen (blur/mozaik) **Python tabanlı bir masaüstü uygulamasıdır.**

Projede, özel olarak belirlenen hassas içeriklerin tespiti için **Roboflow** üzerinde özel bir veri seti (custom dataset) oluşturulmuş ve **YOLOv8** algoritması ile eğitilmiştir.

---

## 🚀 Özellikler

* **Özel Nesne Tespiti (Custom Object Detection):** Roboflow ile etiketlenmiş özel veri seti sayesinde hassas içeriklerin yüksek doğrulukla tespiti.
* **Dinamik Sansürleme:** Tespit edilen nesnelerin koordinatları alınarak, anlık olarak Gauss Bulanıklığı (Gaussian Blur) veya piksel tabanlı mozaikleme uygulanması.
* **Masaüstü Arayüzü:** Kullanıcı dostu, pratik ve modern bir Python masaüstü arayüzü.
* **Görüntü ve Video Desteği:** İster tek bir fotoğraf ister anlık bir video akışı üzerinde gerçek zamanlı sansürleme.

---

## 🛠️ Kullanılan Teknolojiler

* **Programlama Dili:** Python 3.9+
* **Yapay Zeka & Derin Öğrenme:** Ultralytics YOLOv8
* **Veri Seti Yönetimi & Etiketleme:** Roboflow
* **Görüntü İşleme:** OpenCV (cv2)
* **Arayüz Tasarımı:** Tkinter / CustomTkinter

---

## 📦 Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/kullanici-adiniz/goruntu-sansurleme-yolov8.git](https://github.com/kullanici-adiniz/goruntu-sansurleme-yolov8.git)
cd goruntu-sansurleme-yolov8