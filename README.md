# Обрезка ссылок с помощью Битли

Скрипт предназначен для обрезки длинных ссылок с помощью сервиса [Bitly](https://bitly.com), 
а так же для посчета количества переходов по созданным коротким ссылкам (битлинкам).
Подсчет количества переходов работает только с битлинками, сделанными вами.

## Как установить

#### Перед взаимодействием в API Bitly нужно получить токен.

Токен выглядит как строка наподобие следующей: `17c09e20ad155405123ac1977542fecf00231da7`. Bitly предлагает 
несколько видов токенов, но для скрипта, хватит `GENERIC ACCESS TOKEN`. Ссылка для генерации токена указана 
на [странице документации](https://dev.bitly.com).

Python3 должен быть уже установлен.
Для удобства работы и изоляции зависимостей от системы - создайте виртуальное окружение (например с помощью venv)
````
python3 -m venv venv
````
Активируйте виртуальное окружение
````
source venv/bin/activate
````

Затем используйте pip (или pip3, есть конфликт с Python2) 
для установки зависимостей:
```
pip install -r requirements.txt
```
Для скрытия токена используйте файл `.env` и библиотеку `python_dotenv`

## Примеры использования

Запуская скрипт из терминала
```bash
(venv) ➜  api_lesson2 git:(main) python main.py
```
Далее через пробел введем ссылку https://www.google.com/
```
(venv) ➜  api_lesson2 git:(main) python main.py https://www.google.com/
```
После нажатия ENTER мы получим
```
(venv) ➜  api_lesson2 git:(main) python main.py https://www.google.com/
Your billink: https://bit.ly/3o3rfei
```
Мы получили наш битлинк https://bit.ly/3o3rfei

Если мы воспользуемся нашим скриптом и введем этот битлинк? то увидим количество переходом за текущий день 
по этому битлинку

Запустим наш скрипт и введем в него получившуюся ссылку (битлинк)
```
(venv) ➜  api_lesson2 git:(main) ✗ python main.py https://bit.ly/3o3rfei
```
После нажатия ENTER мы получим
````
(venv) ➜  api_lesson2 git:(main) ✗ python main.py https://bit.ly/3o3rfei
Counts: 2
````
Мы видим, что за сегодня по этому битлинку было совершено два перехода

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
