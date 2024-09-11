# Homework_10.1

## Продолжаем работу над виджетом банковских операций клиента. Выкладываем свой проект на GitHub и ведем разработку
   по GitFlow. Учитываем рекомендации PEP 8, продолжаем использовать линтеры и делаем атомарные коммиты.

## Этапы выполнения
1. Создайте новые ветки в вашем репозитории для работы по GitFlow.
2. Создайте новый репозиторий на GitHub, который будет использоваться для хранения и совместной работы над вашим проектом
3. Залейте содержимое вашего локального репозитория в созданный репозиторий на GitHub, используя команды 
   git add , git commit и git push.
4. В директории src вашего проекта создайте модуль processing , который будет содержать новые функции обработки данных.
5. В модуле processing напишите функцию filter_by_state , которая принимает список словарей и опционально значение 
   для ключа state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, 
   у которых ключ state соответствует указанному значению.
6. В том же модуле напишите функцию sort_by_date , которая принимает список словарей и необязательный параметр,
   задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный 
   по дате (date).
7. Создайте README-файл для вашего проекта, в котором описаны цель проекта, инструкции по установке и использованию 
   разработанных функций, примеры работы с ними.
