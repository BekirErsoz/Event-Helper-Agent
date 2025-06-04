
# Eventify Helper

Mini çok‑ajanlı Python paketi: etkinlik planlama, mekân seçimi ve hava durumu bilgisi.

```bash
pip install -r requirements.txt   # Çevrimdışı demo için gerekmez
python -m eventify_helper.main "Merhaba"
```

**Alt ajanlar**

| Ajan | Görev |
|------|-------|
| GreetingAgent | Selamlama / yardım |
| EventSearchAgent | Örnek etkinlik listesi |
| VenueRecommenderAgent | Mekân önerisi |
| WeatherAgent | Basit hava tahmini |

Gerçek API entegrasyonu için `agents/` klasöründeki kodu genişletin.
