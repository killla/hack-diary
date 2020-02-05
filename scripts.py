import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Mark, Chastisement, Commendation, Lesson, Subject



def find_child(name):
    try:
        child = Schoolkid.objects.get(full_name__contains=name)
        return child
    except ObjectDoesNotExist:
        print(f'Ученик {name} не найден!')
    except MultipleObjectsReturned:
        print(f'Найдено несколько учеников с именем {name}!')

def fix_marks(name):
    child = find_child(name)
    if child:
        for current_mark in Mark.objects.filter(schoolkid=child, points__lte=3):
            current_mark.points = 4
            current_mark.save()
        print('Оценки исправлены.')

def remove_chastisements(name):
    child = find_child(name)
    if child:
        all_chastisement = Chastisement.objects.filter(schoolkid=child)
        all_chastisement.delete()
        print('Замечания устранены.')

def create_commendation(name, subject):

    with open('commendations.txt') as commendation_file:
        commendations = commendation_file.readlines()

    child = find_child(name)
    if child:
        if Subject.objects.filter(title=subject, year_of_study=child.year_of_study):
            current_lesson = \
            Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter, subject__title=subject).order_by('-date')[0]
            Commendation.objects.create(text=random.choice(commendations), created=current_lesson.date, schoolkid=child,
                                        subject=current_lesson.subject, teacher=current_lesson.teacher)
            print('Ученик похвален.')
        else:
            print('Предмет не найден')