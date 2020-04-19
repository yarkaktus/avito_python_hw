### Install
```shell script
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Homework 3
#### Issue 1
```shell script
python -m doctest -o NORMALIZE_WHITESPACE hw3/morse.py
```
#### Issue 2
```shell script
python -m pytest hw3/tests/test_morse_decode_pytest.py
```

#### Issue 3
```shell script
python -m unittest hw3/tests/test_fit_transform_unittest.py
```

#### Issue 4
```shell script
python -m pytest hw3/tests/test_fit_transform_pytest.py
```
#### Issue 5
```shell script
python -m unittest hw3/tests/test_what_is_year_now_unittest.py
```
Запуск анализа покрытия
```shell script
python -m pytest --cov . --cov-report html
```

### Homework 4
Запуск тестов
```shell script
python -m pytest hw4 --doctest-modules
```

### Homework 5
Запуск тестов
```shell script
python -m pytest hw5
```