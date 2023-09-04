import config

def no_data(current_date):

    return f'Нет ответов на отзывы за текущую дату ({current_date}).'


def status_text():
    if config.ACTIVE:
        status = '*активен*'
        command = 'Используйте */deactivate* для отключения.'
    else:
        status = '*не активен*'
        command = 'Используйте */activate* для активации.'
    
    return f'Бот {status}. {command}'

PROHIBITED = 'У вас недостаточно прав.'

ACTIVATED = 'Бот *активирован.*\nИспользуйте */deactivate* для отключения.'

DEACTIVATED = 'Бот *деактивирован.*\nИспользуйте */activate* для активации.'

WRONG_FORMAT = 'Неверный формат даты. Укажите дату в формате *дд.мм.гггг* (н.р. 01.09.2023).'

NO_ANSWERS = 'Нет ответов на отзывы.'