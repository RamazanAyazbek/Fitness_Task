from django.db import models



class Client(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class GymRoom(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    dob=models.DateField()

    GENDER_CHOICES=(
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    experience=models.IntegerField()
    

    def __str__(self):
        return f'{self.name} {self.surname}'


class Schedule(models.Model):
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
    gym_room=models.ForeignKey(GymRoom, on_delete=models.CASCADE)
    start_time=models.TimeField()
    end_time=models.TimeField()

    def __str__(self):
        return f"{self.trainer} {self.start_time} {self.end_time}"

class Appointment(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    schedule=models.ForeignKey(Schedule, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.client.name} in {self.schedule.gym_room}"


    












