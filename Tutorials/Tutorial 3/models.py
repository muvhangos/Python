from django.db import models

class ServiceRequest(models.Model):
    ROOM_SERVICE_CHOICES = [
        ('cleaning', 'Room Cleaning'),
        ('maintenance', 'Maintenance'),
        ('food', 'Food Service'),
    ]

    room_number = models.CharField(max_length=10)
    guest_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=20, choices=ROOM_SERVICE_CHOICES)
    details = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest_name} - {self.request_type} (Room {self.room_number})"
