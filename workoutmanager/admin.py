from django.contrib import admin
from .models import Client, Trainer, GymRoom, Schedule, Appointment



class ScheduleAdmin(admin.ModelAdmin):
    list_display=('trainer', 'gym_room', 'start_time', 'end_time')
    def save_model(self, request, obj, form, change):
        existing_schedules=Schedule.objects.filter(gym_room=obj.gym_room, start_time=obj.start_time)
        if existing_schedules.exists():
            existing_schedules=existing_schedules.first()
            if existing_schedules.trainer!=obj.trainer:
                raise ValueError(
                    f'Тренажерный зал {obj.gym_room}  уже запланирован на {existing_schedules.trainer} в {obj.start_time}'
                )
        obj.save()



class AppointmentAdmin(admin.ModelAdmin):
    list_display=('client', 'gym_room', 'start_time', 'end_time', 'trainer')


    def gym_room(self, obj):
        return obj.schedule.gym_room

    def start_time(self, obj):
        return obj.schedule.start_time

    def end_time(self, obj):
        return obj.schedule.end_time

    def trainer(self, obj):
        return obj.schedule.trainer
    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name =='schedule':
            kwargs['queryset']=Schedule.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    

    def save_model(self, request, obj, form, change):
        if not obj.schedule:
            raise ValueError('Выберите расписание')
        obj.gym_room=obj.schedule.gym_room
        obj.start_time=obj.schedule.start_time
        obj.end_time=obj.schedule.end_time

        obj.save()

class TrainerAdmin(admin.ModelAdmin):
    list_display=('name', 'surname', 'dob', 'experience')


admin.site.register(Client)
admin.site.register(GymRoom)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Appointment, AppointmentAdmin)






