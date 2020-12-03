FROM python:3.8-slim

LABEL author="Oleh"
LABEL version=1.0

# оновлюємо систему
RUN sudo apt-get update && sudo apt-get upgrade -y

# Встановлюємо потрібні пакети
RUN sudo apt-get install git -y && sudo pip install pipenv

# Створюємо робочу папку
WORKDIR /Lab4

# Завантажуємо файли з Git
RUN git clone https://github.com/Oleh-Voloshchuk/TPIS/tree/main/Lab3

# Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
WORKDIR /app
RUN cp -r /Lab4/TPIS/Lab3/* .

# Інсталюємо всі залежності
RUN pipenv install

# Відкриваємо порт 8000 на зовні
EXPOSE 8000

# Це команда яка виконається при створенні контейнера
ENTRYPOINT ["pipenv", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000"]