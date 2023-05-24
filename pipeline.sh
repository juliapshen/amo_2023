#!/bin/bash
echo 'запуск скрипта создания данных'
python3 data_creation.py
echo 'запуск скрипта обработки и стандартизации данных'
python3 model_preprocessing.py
echo 'запуск скрипта создания модели и обучения'
python3 model_preparation.py
echo 'запуск скрипта создания модели и обучения'
python3 model_testing.py