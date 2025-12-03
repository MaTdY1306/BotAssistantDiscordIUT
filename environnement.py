import pytz
from datetime import datetime

class Environnement:

    def __init__(self):
        self.mois = [
            'janvier',
            'février',
            'mars',
            'avril',
            'mai',
            'juin',
            'juillet',
            'août',
            'septembre',
            'octobre',
            'novembre',
            'décembre'
            ]
        
        self.timezone : pytz.timezone = pytz.timezone("Europe/Paris")
        self.now = datetime.now(tz=self.timezone)

