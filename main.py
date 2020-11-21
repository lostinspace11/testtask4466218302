import json
import jsonschema
from loguru import logger
import os


@logger.catch
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
    logger.info("Event is OK\n=================================")


def main():
    """Проходим по папке task_folder в поисках файлов с расширениями .schema и .json и доабавляем пути к ним в списки.
    Далее, для каждого event производим валидацию с каждой схемой.
    Результат записывается в папку log для каждой схемы отдельно.
    """
    os.chdir('task_folder')
    schemas, events = [], []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith('.schema'):
                schemas.append(os.path.join(root, name))
            if name.endswith('.json'):
                events.append(os.path.join(root, name))
    for schema in schemas:
        logger.add(f'logs{schema}.log', format="{time} {level} {message}")
        logger.info(f"SCHEMA: {schema}\n=================================")
        for event in events:
            logger.info(f"Validation of event: {event}\n")
            validate_event(event, schema)


main()
