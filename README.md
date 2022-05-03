# autobio
Бот для автоматического изменения био по шаблону

# Шаблон
Он находится в файле `config.py`:

`TEMPLATE = "Привет / {hour}:{minute} ({timezone} {tzname})"`

Доступные параметры:

* {hour} - текущий час
* {minute} - текущая минута
* {day} - текущий день
* {month} - текущий месяц
* {year} - текущий год
* {timezone} - часовой пояс
* {tzname} - название часового пояса

# Как это выглядит
![изображение](https://user-images.githubusercontent.com/48158038/166441750-b93168a7-31a3-425c-bc9a-e8deb2ae05be.png)

# Запуск
`python3 main.py`
