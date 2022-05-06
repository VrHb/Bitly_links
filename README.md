# Получение коротких ссылок с помощью API Bitly

Программа работает на python версии 3.10, вы вводите ссылку, получаете короткую, более читаемую версию, либо количество кликов по ссылке, если она обработана сервисом bitly

### Как установить:

* Необходимо установить интерпретатор python
* Скопировать содержимое проекта к себе в рабочую директорию
* Активировать внутри рабочей директории виртуальное окружение:

```
python -m venv [название окружения]
```
* Установить зависимости(необходимые библиотеки):

```
pip install -r pip_requirements.txt
```

### Как пользоваться:

Запустить такой командой:

```
python [имя файла] [ссылка на ресурс]
```

Пример запуска:
```
python main.py https://gist.github.com/
```

Программа выведет в терминал результат



