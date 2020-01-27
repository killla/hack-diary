import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson

commendation_list = []
with open('commendations.txt') as commendation_file:
    for commendation in commendation_file:
        commendation_list.append(commendation)

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
    while Mark.objects.filter(schoolkid=child, points__lte=3):
        current_mark = Mark.objects.filter(schoolkid=child, points__lte=3)[0]
        current_mark.points = 4
        current_mark.save()
    print('Оценки исправлены.')

def remove_chastisements(name):
    child = find_child(name)
    all_Chastisement = Chastisement.objects.filter(schoolkid=child)
    all_Chastisement.delete()
    print('Замечания устранены.')

def create_commendation(name, subject):
    child = find_child(name)
    current_lesson = \
    Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter, subject__title=subject).order_by('-date')[0]
    Commendation.objects.create(text=random.choice(commendation_list), created=current_lesson.date, schoolkid=child,
                                subject=current_lesson.subject, teacher=current_lesson.teacher)
    print('Ученик похвален.')