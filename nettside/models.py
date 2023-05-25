from django.db import models

# Samme som "CREATE TABLE Laptop"
class Laptop(models.Model):
    # leverandor varchar(20)
    leverandor = models.CharField(max_length=20)
    modell = models.CharField(max_length=20)

    # IntegerField() trenger ikke max_length keywordet
    serienummer = models.IntegerField()

    # Her må vi neste en tuple ikke i status_choices for å legge de til som ett valg. Den første strengen er det databasen lagrer statusen som, mens den andre strengen defingerer det som blir vist.
    status_choices = (
        ("ut", "Utlånt"),
        ("iut", "Ikke utlånt")
    ) 
    status = models.CharField(max_length=12, choices=status_choices)
    #                                                   ^^
    #                                 Her gir vi inn alle valgene.

    # blank og null gør at dette feltet blir ikke-obligatorisk å fylle ut.
    notater = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.leverandor} {self.modell} {self.status}"