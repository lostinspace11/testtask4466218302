Тестовое задание на позицию Junior back-end developer
=====================
Задание
-----------------------------------
Необходимо написать скрипт, который сможет найти максимальное количество ошибок структуры и данных в первой папке.<br>
Лог лежит в файле validate.log
***
### Таблица валидности файлов для каждой схемы:
| File | cmarker_created.schema |	label_selected.schema | sleep_created.schema | workout_created.schema |	
|-------------------------------------------|:-:|:-:|:-:|:-:|
| 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json | + | - | + | - | 
| 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json | + | - | + | - | 
| 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json | - | - | - | - | 
| 2e8ffd3c-dbda-42df-9901-b7a30869511a.json | + | - | + | - | 
| 3ade063d-d1b9-453f-85b4-dda7bfda4711.json | + | - | + | - | 
| 3b4088ef-7521-4114-ac56-57c68632d431.json | + | - | + | - | 
| 6b1984e5-4092-4279-9dce-bdaa831c7932.json | + | - | + | - | 
| a95d845c-8d9e-4e07-8948-275167643a40.json | + | - | + | - | 
| ba25151c-914f-4f47-909a-7a65a6339f34.json | + | - | + | - | 
| bb998113-bc02-4cd1-9410-d9ae94f53eb0.json | + | - | + | - | 
| c72d21cf-1152-4d8e-b649-e198149d5bbb.json | + | - | + | - | 
| cc07e442-7986-4714-8fc2-ac2256690a90.json | + | - | + | - | 
| e2d760c3-7e10-4464-ab22-7fda6b5e2562.json | + | - | + | - | 
| f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json | + | - | + | - | 
| fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json | + | - | + | - | 
| ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json | - | - | + | - | 

### Ошибки json-файлов при валидации схемой cmarker_created.schema
Схема:
```
{
     '$schema': 'http://json-schema.org/schema#',
     'properties': {'cmarkers': {'items': {'properties': {'date': {'type': 'string'},
                                                          'id': {'type': 'integer'},
                                                          'slug': {'type': 'string'}},
                                           'required': ['date',
                                                        'id',
                                                        'slug'],
                                           'type': ['object', 'string']},
                                 'type': 'array'},
                    'datetime': {'type': 'string'},
                    'user_id': {'type': 'integer'}},
     'required': ['cmarkers', 'datetime', 'user_id'],
     'type': 'object'
}
```

#### Файл: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json<br>
Ошибки: 
1. ERROR None is not of type 'object'<br>
Вывод: файл пустой
------
#### Файл: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json<br>
Ошибки: 
```
ERROR None is not of type 'integer'
Failed validating 'type' in schema['properties']['user_id']:
    {'type': 'integer'}
On instance['user_id']:
    None
```
Вывод: Значение user_id должно быть целочисленным

### Ошибки json-файлов при валидации схемой cmarker_created.schema
Схема:
```
{'$schema': 'http://json-schema.org/schema#',
     'properties': {'id': {'type': ['null', 'integer']},
                    'labels': {'items': {'properties': {'category': {'type': ['null',
                                                                              'string']},
                                                        'color': {'type': ['null',
                                                                           'object']},
                                                        'is_custom_tag': {'type': 'boolean'},
                                                        'name_en': {'type': 'string'},
                                                        'name_ru': {'type': 'string'},
                                                        'property_arousal': {'type': ['string',
                                                                                      'null']},
                                                        'property_pleasure': {'type': ['string',
                                                                                       'null']},
                                                        'property_stability': {'type': ['string',
                                                                                        'null']},
                                                        'property_vitality': {'type': ['string',
                                                                                       'null']},
                                                        'property_where': {'type': ['string',
                                                                                    'null']},
                                                        'slug': {'type': 'string'},
                                                        'type': {'type': 'integer'},
                                                        'type_stress': {'type': 'integer'}},
                                         'required': ['category',
                                                      'color',
                                                      'is_custom_tag',
                                                      'name_en',
                                                      'name_ru',
                                                      'property_arousal',
                                                      'property_pleasure',
                                                      'property_stability',
                                                      'property_vitality',
                                                      'property_where',
                                                      'slug',
                                                      'type',
                                                      'type_stress'],
                                         'type': 'object'},
                               'type': 'array'},
                    'rr_id': {'type': ['null', 'integer']},
                    'timestamp': {'type': 'string'},
                    'unique_id': {'type': 'string'},
                    'user': {'properties': {'id': {'type': 'integer'}},
                             'required': ['id'],
                             'type': 'object'},
                    'user_id': {'type': 'integer'}},
     'required': ['id',
                  'labels',
                  'rr_id',
                  'timestamp',
                  'unique_id',
                  'user',
                  'user_id'],
     'type': 'object'}
```

#### Файл: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json<br>
Ошибки: 
``'user' is a required property``<br>
Вывод: Добавить обязательную запись **user**<br>

#### Файл: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json<br>
Ошибки: 
```
'297e4dc6-07d1-420d-a5ae-e4aff3aedc19' is not of type 'null', 'integer'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
 ```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число

#### Файл: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json<br>
Ошибки: 
1. ERROR None is not of type 'object'<br>
Вывод: файл пустой

#### Файл: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json<br>
Ошибки: 
```
'2e8ffd3c-dbda-42df-9901-b7a30869511a' is not of type 'null', 'integer'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число

#### Файл: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json<br>
Ошибки: 
```
'3ade063d-d1b9-453f-85b4-dda7bfda4711' is not of type 'null', 'integer'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число


#### Файл: 3b4088ef-7521-4114-ac56-57c68632d431.json<br>
Ошибки: 
```
'3b4088ef-7521-4114-ac56-57c68632d431' is not of type 'null', 'integer'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число

#### Файл: 6b1984e5-4092-4279-9dce-bdaa831c7932.json<br>
Ошибки: 
```
'1fe93f66-eaa8-11ea-a179-58e81c50ca6b' is not of type 'null', 'integer'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число

#### Файл: a95d845c-8d9e-4e07-8948-275167643a40.json<br>
Ошибки: 
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**

#### Файл: ba25151c-914f-4f47-909a-7a65a6339f34.json<br>
Ошибки: 
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**

#### Файл: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json<br>
Ошибки: 
```
'bb998113-bc02-4cd1-9410-d9ae94f53eb0' is not of type 'null', 'integer'r'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число

#### Файл: c72d21cf-1152-4d8e-b649-e198149d5bbb.json<br>
Ошибки: 
```
'c72d21cf-1152-4d8e-b649-e198149d5bbb' is not of type 'null', 'integer'r'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число

#### Файл: cc07e442-7986-4714-8fc2-ac2256690a90.json<br>
Ошибки: 
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**

#### Файл: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json<br>
Ошибки: 
```
'e2d760c3-7e10-4464-ab22-7fda6b5e2562' is not of type 'null', 'integer'r'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число

#### Файл: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json<br>
Ошибки: 
```
'f5656ff6-29e1-46b0-8d8a-ff77f9cc0953' is not of type 'null', 'integer'r'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число

#### Файл: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json<br>
Ошибки: 
```
'fb1a0854-9535-404d-9bdd-9ec0abb6cd6c' is not of type 'null', 'integer'r'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`

Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число

#### Файл: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json<br>
Ошибки: 
```
'ffe6b214-d543-40a8-8da3-deb0dc5bbd8c' is not of type 'null', 'integer'r'
Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}
```
`ERROR 'user' is a required property`
```
None is not of type 'integer'

Failed validating 'type' in schema['properties']['user_id']:
    {'type': 'integer'}
```
Вывод: 
1. Добавить обязательную запись **user**
2. Изменить id на null или целое число
3. Изменить user_id на целое число

### Ошибки json-файлов при валидации схемой sleep_created.schema
Схема:
```
 {'$schema': 'http://json-schema.org/schema#',
     'properties': {'activity_type': {'type': 'string'},
                    'finish_time': {'type': 'string'},
                    'info': {'items': {'properties': {'type': {'type': 'string'},
                                                      'value': {'type': 'number'}},
                                       'required': ['type', 'value'],
                                       'type': 'object'},
                             'type': 'array'},
                    'phases_info': {'items': {'properties': {'duration': {'type': 'number'},
                                                             'percent': {'type': 'number'},
                                                             'type': {'type': 'string'}},
                                              'required': ['duration',
                                                           'percent',
                                                           'type'],
                                              'type': 'object'},
                                    'type': 'array'},
                    'points': {'items': {'properties': {'x_date': {'type': 'string'},
                                                        'y_value': {'type': 'number'}},
                                         'required': ['x_date', 'y_value'],
                                         'type': 'object'},
                               'type': 'array'},
                    'source': {'type': 'string'},
                    'time_start': {'type': 'string'},
                    'timestamp': {'type': 'string'},
                    'type_ranges': {'items': {'properties': {'date': {'type': 'string'},
                                                             'type': {'type': 'string'}},
                                              'required': ['date', 'type'],
                                              'type': 'object'},
                                    'type': 'array'},
                    'unique_id': {'type': 'string'}},
     'required': ['source',
                  'timestamp',
                  'finish_time',
                  'activity_type',
                  'time_start',
                  'unique_id'],
     'type': 'object'}
```

#### Файл: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json<br>
Ошибки: 
1. ERROR None is not of type 'object'<br>
Вывод: файл пустой

### Ошибки json-файлов при валидации схемой workout_created.schema
Схема: 
```
{'$schema': 'http://json-schema.org/schema#',
     'properties': {'activity_name': {'type': 'string'},
                    'activity_type': {'type': 'string'},
                    'calories': {'type': 'integer'},
                    'calories_active': {'type': 'number'},
                    'calories_basal': {'type': 'number'},
                    'distance': {'type': 'integer'},
                    'duration': {'type': 'number'},
                    'exercise_time': {'type': 'integer'},
                    'met': {'type': 'number'},
                    'pace_avg': {'type': 'number'},
                    'pulse': {'type': 'integer'},
                    'pulse_max': {'type': ['null', 'integer']},
                    'pulse_min': {'type': ['null', 'integer']},
                    'resting_hr': {'type': 'integer'},
                    'source': {'type': 'string'},
                    'speed_avg': {'type': 'number'},
                    'steps': {'type': 'integer'},
                    'steps_speed_avg': {'type': 'number'},
                    'steps_speed_max': {'type': 'number'},
                    'time_end': {'type': 'string'},
                    'time_start': {'type': 'string'},
                    'timestamp': {'type': 'string'},
                    'type_ranges': {'properties': {'cardio': {'type': 'integer'},
                                                   'fat_burn': {'type': 'integer'},
                                                   'hardcore': {'type': 'integer'},
                                                   'warm_up': {'type': 'integer'}},
                                    'required': ['cardio',
                                                 'fat_burn',
                                                 'hardcore',
                                                 'warm_up'],
                                    'type': 'object'},
                    'unique_id': {'type': 'string'}},
     'required': ['activity_name',
                  'activity_type',
                  'source',
                  'time_end',
                  'time_start',
                  'timestamp',
                  'unique_id'],
     'type': 'object'}
```

#### Файл: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**


#### Файл: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**

#### Файл: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json<br>
Ошибки: 
1. ERROR None is not of type 'object'<br>
Вывод: файл пустой

#### Файл: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**

#### Файл: 3b4088ef-7521-4114-ac56-57c68632d431.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**

#### Файл: 6b1984e5-4092-4279-9dce-bdaa831c7932.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**


#### Файл: a95d845c-8d9e-4e07-8948-275167643a40.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**

#### Файл: ba25151c-914f-4f47-909a-7a65a6339f34.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**


#### Файл: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**

#### Файл: c72d21cf-1152-4d8e-b649-e198149d5bbb.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**


#### Файл: cc07e442-7986-4714-8fc2-ac2256690a90.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**

#### Файл: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**

#### Файл: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**


#### Файл: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**

#### Файл: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json<br>
Ошибки: 
`'type_ranges' is a required property`

Вывод: 
1. Добавить обязательную запись **type_ranges**

