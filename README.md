# Tic-Tac-Toe & Web Client

![Tic-Tac-Toe](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKjB1hvlWANB_ZnLbvhxIKwBCtkAbZJZcl-w&s)

## 📚 Цель проекта

Проект "Крестики-нолики" создан для изучения технологий веб-разработки, таких как Django и JavaScript. Этот проект демонстрирует, как можно создать чтобы обеспечить полное взаимодействие с пользователем в реальном времени.

## 🌟 Функциональность


- **Сделать ход**: Клиентское приложение позволяет игрокам делать ходы и видеть обновления в реальном времени.
- **Проверка победителя**: Игра автоматически проверяет победителя после каждого хода и отображает результат.
- **Интуитивный интерфейс**: Современный и простой интерфейс для легкого взаимодействия.

## 🖼️ Скриншоты

<a href="https://ibb.co/djn81ST"><img src="https://i.ibb.co/RYLRZ1F/Screenshot-2024-07-03-at-16-28-43.png" alt="Screenshot-2024-07-03-at-16-28-43" border="0"></a>

*Пример интерфейса игры "Крестики-нолики".*

## 🚀 Установка и запуск

## Установка зависимостей
Убедитесь, что у вас установлен Python. Затем создайте виртуальное окружение и установите необходимые зависимости:

```bash
python -m venv venv
source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
pip install -r requirements.txt
```
## Применение миграций

Создайте базы данных и примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```
## Запуск сервера разработки
<b>Запустите сервер разработки Django:</b>
```bash
python manage.py runserver
```
Следуйте этим шагам, чтобы запустить проект локально.

## 📂 Структура проекта

```
tictactoe/
│
├── tictactoe/             # Основная директория проекта Django
│   ├── __init__.py
│   ├── settings.py        # Настройки Django
│   ├── urls.py            # Маршруты
│   ├── wsgi.py
│   └── asgi.py
│
├── game/                  # Приложение Django для управления игрой
│   ├── migrations/        # Миграции базы данных
│   ├── models.py          # Модели базы данных
│   ├── views.py           # Представления 
│   ├── urls.py            # Маршруты 
│   ├── tests.py           # Тесты
│   ├── static/                # Статические файлы (HTML, CSS, JS)
│   │   ├──img/                # Папка с изображениями
│   │   ├── css/               # стили для шаблона 
│   │   └── js/                # javascirtp code
│   ├── templates/
│   │   ├──components/         # компоненты
│   │   ├── pages/             # основные страницы 
│   │   └── base.html/         # базовый страница
│   │ 
├── user/                  # Приложение Django для управления users
│   ├── migrations/        # Миграции базы данных
│   ├── models.py          # Модели базы данных
│   ├── views.py           # Представления 
│   ├── urls.py            # Маршруты 
│   ├── tests.py           # Тесты
│   └── static/                # Статические файлы (HTML, CSS, JS)
│   │   ├── index.html
│   │   ├──img/                # Папка с изображениями
│   │   ├── css/               # стили для шаблона 
│   │   └── js/                # javascirtp code 
│   ├── templates/             # шаблоны для страницы
│   │   ├──components/         # компоненты
│   │   ├── pages/             # основные страницы 
│   │   └── base.html/         # базовый страница
│   │ 
│
├── manage.py              # Команда управления Django
├── requirements.txt       # Зависимости проекта
└── README.md              # Документация проекта

```

### 1. Клонирование репозитория

Клонируйте этот репозиторий на ваш локальный компьютер:

```bash
git clone https://github.com/username/tictactoe.git
cd tictactoe
