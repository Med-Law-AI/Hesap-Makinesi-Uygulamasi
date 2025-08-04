# Hesap Makinesi Uygulaması

Bu proje, FastAPI ile geliştirilmiş basit bir hesap makinesi API'si ve HTML/JavaScript/CSS ile hazırlanmış bir web arayüzünden oluşmaktadır.

## Özellikler

- Toplama, çıkarma, çarpma ve bölme işlemleri
- API üzerinden işlem yapma
- Web arayüzü ile kolay kullanım

## Kurulum

1. **Projeyi klonlayın:**
   ```
   git clone https://github.com/Med-Law-AI/Hesap-Makinesi-Uygulamas-.git
   cd Hesap-Makinesi-Uygulaması
   ```

2. **Gerekli paketleri yükleyin:**
   ```
   pip install fastapi uvicorn pydantic
   ```

3. **Sunucuyu başlatın:**
   ```
   uvicorn main:app --reload
   ```

4. **Web arayüzünü açın:**
   - `index.html` dosyasını tarayıcıda açın.
   - Formu doldurup "Hesapla"ya tıklayın.

## API Kullanımı

- **POST /calculate**
  - Gövde (JSON):
    ```json
    {
      "number1": 10,
      "number2": 5,
      "operation": "+"
    }
    ```
  - Dönen Sonuç:
    ```json
    {
      "İşlem Sonucu": 15
    }
    ```

## Notlar

- CORS ayarı FastAPI'de otomatik olarak eklenmiştir.
- Sunucu `localhost:8000` adresinde çalışır.
- Farklı port veya adres kullanıyorsanız, `index.html` içindeki JS kodunu güncelleyin.

## Katkı

Katkıda bulunmak için fork'layıp pull request gönderebilirsiniz.

##