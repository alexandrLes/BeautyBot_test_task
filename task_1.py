import re

def verify_text(test_text, list_keys):
    # Найдем все ключи в фигурных скобках
    pattern = r'\{([^}]+)\}'
    found_keys = re.findall(pattern, test_text)
    
    for key in found_keys:
        if key not in list_keys:
            return f"Ошибка: некорректный ключ {key}"

    open_brackets = test_text.count('{')
    close_brackets = test_text.count('}')
    if open_brackets != close_brackets:
        return "Ошибка: несоответствие количества открывающих и закрывающих скобок"
    
    return "Все проверки пройдены"

test_text = '''{name}, ваша запись изменена:
Время: {day_month} в {start_time}
Мастер: {master}
Услуги: {services}
управление записью {record_link}'''
list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']

result = verify_text(test_text, list_keys)
print(result)
