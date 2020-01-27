# Взламываем электронный дневник

## Запуск
Для запуска скриптов необходимо проделать следующи действия:
- Перейти в папку электронного дневника содержащую файл `manage.py`
- Положить в эту папку файл commendations.txt
- Запустить в терминале консоль Django командой `python manage.py shell`
- Ввести команду скрипта

После выполнения команды на экран будет выведен результат.

## Команды 
`fix_marks` - исправление у указанного ученика всех оценок `2` и `3` на `4`

`remove_chastisements` - удаление всех замечаний ученика

`create_commendation` - добавление похвалы указанному ученику по указанному предмету

## Примеры команд
`fix_marks('Васильева Полина')`

`remove_chastisements('Рожков Святополк')`

`create_commendation('Жданов Викторин', 'Технология')`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
