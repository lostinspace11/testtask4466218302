import json
import jsonschema
from loguru import logger
import os


def validate_event(event_path, schema_path):
    """Десериализируем json из файлов.
    Создаем объект Draft3Validator и проверяем event на валидность.
    Результаты записываем в логи."""
    with open(event_path) as ep, open(schema_path) as sp:
        json_event = json.load(ep)
        json_schema = json.load(sp)
    validator = jsonschema.Draft3Validator(json_schema)
    if not validator.is_valid(json_event):
        logger.error("There are some errors in the event: ")
        for error in validator.iter_errors(json_event):
            logger.error(f"{error}\n=================================")
        return False
    logger.info("Event is OK\n=================================")
    return True


def validate_schema(schema_path, event_path):
    """Проверка схемы на ошибки.
    Если при вызове метода validate вызывается исключение jsonschema.exceptions.SchemaError,
    то схема имеет ошибки"""
    with open(event_path) as ep, open(schema_path) as sp:
        json_event = json.load(ep)
        json_schema = json.load(sp)
    try:
        jsonschema.validate(json_event, json_schema)
    except jsonschema.exceptions.SchemaError:
        logger.info(f"Schema {schema_path} is INVALID")
        return False
    except jsonschema.exceptions.ValidationError:
        logger.info(f"Schema {schema_path} is OK")
        return True
    else:
        logger.info(f"Schema {schema_path} is OK")
        return True


def main():
    """Проходим по папке task_folder в поисках файлов с расширениями .schema и .json и добавляем пути к ним в списки.
    Проверяем каждую схему на правильность.
    Далее, для каждого event производим валидацию с каждой схемой.
    Результат записывается в папку log для каждой схемы отдельно.
    """
    logger.add('validation.log', format="{time} {level} {message}")
    os.chdir('task_folder')
    schemas, events = [], []

    # Проход директории и поиск нужных файлов
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith('.schema'):
                schemas.append(os.path.join(root, name))
            if name.endswith('.json'):
                events.append(os.path.join(root, name))
    result_table = {}
    valid_schemas, invalid_schemas = [], []

    # Проверяем схемы на ошибки
    for schema in schemas:
        if validate_schema(schema, events[0]):
            valid_schemas.append(schema)
        else:
            invalid_schemas.append(schema)

    # Валидация json-файлов
    for schema in valid_schemas:
        logger.info(f"SCHEMA: {schema}\n=================================")
        for event in events:
            result_table[event] = result_table.get(event, {})
            logger.info(f"Validation of event: {event}\n")
            result_table[event][schema] = validate_event(event, schema)

    # Вывод таблицы валидности json-файлов
    print(f'| File |', end='\t')
    for schema in schemas:
        print(f' {schema} |', end=' ')
    print('\n')
    for key in result_table:
        print(f'| {key} |', end=' ')
        for k, v in result_table[key].items():
            print('+ |' if v else '- |', end=' ')
        print('\n')


main()
