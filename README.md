#  Carwash Web App

A **Django** application for managing a carwash business. It provides user authentication, booking services, and admin control over services, locations, bookings, and users.

---
![image](https://github.com/user-attachments/assets/862dfc97-698c-418e-ac29-a7ab8cdd22f6)



##  Features

-  **User Accounts** – Register, login, logout using Django’s built-in auth.
-  **Service Catalog** – Define and manage carwash services and locations.
-  **Booking System** – Users can schedule and track carwash bookings.
-  **Admin Dashboard** – Admins manage services, locations, bookings, and user permissions.
-  **Booking States** – Tracks statuses like pending, confirmed, or rejected.

---
![image](https://github.com/user-attachments/assets/80b8d4f6-ac0a-44c8-810e-3b230e91e630)
![image](https://github.com/user-attachments/assets/4bb36367-97f9-451f-ae52-589420701a1e)
![image](https://github.com/user-attachments/assets/f133f2d2-5d03-4713-b19d-47fe501f6281)
![image](https://github.com/user-attachments/assets/46bc2582-6198-45a4-ba4b-270b006dae0e)



##  Tech Stack

- Python 3.x
- Django (check `requirements.txt` for exact version)
- SQLite (default dev DB; swap for Postgres/MySQL in production)
- Optional: Bootstrap or any CSS framework in templates

---

##  Installation

1. **Clone the repository**
git clone https://github.com/khatszianAli/Django-project.git  
cd Django-project/Carwash    
2. Set up virtual environment    
python -m venv venv    
source venv/bin/activate  # macOS/Linux    
 OR: venv\Scripts\activate  # Windows    
3. Install dependencies    
pip install -r requirements.txt    
4. Apply database migrations    
python manage.py makemigrations    
python manage.py migrate    
5. Create a superuser    
python manage.py createsuperuser    
6. Run the development server    
python manage.py runserver    
Visit the app at http://127.0.0.1:8000/ and Django Admin at http://127.0.0.1:8000/admin/.  


## Usage  
Register a user or log in via admin-defined accounts.    
Browse services and locations.  
Create new bookings and track status.  
Admins use /admin/ panel for full control over models.  

# Carwash Web App

Приложение **Django** для управления автомоечным бизнесом. Оно обеспечивает аутентификацию пользователей, услуги бронирования и административный контроль над услугами, местоположениями, бронированиями и пользователями.

---
![image](https://github.com/user-attachments/assets/862dfc97-698c-418e-ac29-a7ab8cdd22f6)

## Функции

- **Учетные записи пользователей** — регистрация, вход в систему, выход из системы с использованием встроенной аутентификации Django.

- **Каталог услуг** — определение и управление услугами и местоположениями автомоек.

- **Система бронирования** — пользователи могут планировать и отслеживать бронирования автомоек.

- **Панель администратора** — администраторы управляют услугами, местоположениями, бронированиями и разрешениями пользователей.

- **Состояния бронирования** — отслеживает такие статусы, как «ожидание», «подтверждено» или «отклонено».

---
![image](https://github.com/user-attachments/assets/80b8d4f6-ac0a-44c8-810e-3b230e91e630)
![image](https://github.com/user-attachments/assets/4bb36367-97f9-451f-ae52-589420701a1e)
![image](https://github.com/user-attachments/assets/f133f2d2-5d03-4713-b19d-47fe501f6281)
![image](https://github.com/user-attachments/assets/46bc2582-6198-45a4-ba4b-270b006dae0e)

## Технологии Stack

- Python 3.x
- Django (проверьте `requirements.txt` для точной версии)
- SQLite (база данных dev по умолчанию; замените Postgres/MySQL в production)
- Дополнительно: Bootstrap или любой CSS-фреймворк в шаблонах

---

## Установка

1. **Клонируйте репозиторий**  
git clone https://github.com/khatszianAli/Django-project.git    
cd Django-project/Carwash    
2. Настройте виртуальную среду    
python -m venv venv    
source venv/bin/activate # macOS/Linux  
ИЛИ: venv\Scripts\activate # Windows  
3. Установите зависимости  
pip install -r requirements.txt  
4. Примените миграции базы данных  
python manage.py makemigrations  
python manage.py migrate  
5. Создайте суперпользователя  
python manage.py createsuperuser  
6. Запустите сервер разработки  
python manage.py runserver  
Посетите приложение по адресу http://127.0.0.1:8000/ и Django Admin по адресу http://127.0.0.1:8000/admin/.  

## Использование  
Зарегистрируйте пользователя или войдите через учетные записи, определенные администратором.      
Просмотр услуг и местоположений.    
Создание новых бронирований и отслеживание статуса.    
Администраторы используют панель /admin/ для полного контроля над моделями.    
