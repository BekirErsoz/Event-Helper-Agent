
import random, datetime
class WeatherAgent:
    def respond(self, _message: str) -> str:
        today = datetime.date.today().strftime('%d %B %Y')
        condition = random.choice(['güneşli', 'parçalı bulutlu', 'yağmurlu', 'kapalı'])
        temp = random.randint(17, 30)
        return f"{today} İstanbul için hava {condition}, sıcaklık ≈ {temp}°C."
