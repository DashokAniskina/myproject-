## Проект по django "Запись на тестдрайв"
### Руководство пользователя
проект представляет собой сайт из трех страниц с функцией записи на тестдрайв
<img width="594" height="61" alt="image" src="https://github.com/user-attachments/assets/6de03d4d-660a-47a9-a96a-82071782a7ca" />

на главной странице отображаются активные записи клиента 
<img width="706" height="472" alt="image" src="https://github.com/user-attachments/assets/164b11e2-3d78-43a1-89d2-2e18f0becb12" />

страница "О компании" содержит описание деятельности компании
<img width="1129" height="547" alt="image" src="https://github.com/user-attachments/assets/17b0e52b-832d-4ff7-835a-389bb8449288" />

для записи на тестдрайв нужно перейти на страницу "Тестдрайв" и заполнить форму
<img width="676" height="354" alt="image" src="https://github.com/user-attachments/assets/8b40ebba-50df-4844-ab88-110050b46a79" />

после заполнения формы и ее отправки новая запись появится на главной странице
<img width="659" height="492" alt="image" src="https://github.com/user-attachments/assets/28addc6a-a948-437a-b31b-6286acc6487e" />

### Руководство программиста 
> Django - высокоуровненвый веб-фреймворк, который позволяет быстро создавать безопасные и поддерживаемые сайты
Начало работы со средой:
 '''
# создаю виртуальную среду
python -m venv .venv
# активирую виртуальную среду
venv\Scripts\activate
# устанавливаю библиотеку
pip install django==5
# создаю проект
django-admin startproject testdrive
# Перехожу в папке проекта
cd testdrive
# Создаю приложение
python manage.py startapp myapp
# Перейдите в файл settings.py и в разделе INSTALLED_APPS впишите (вконце) название приложения "myapp"
# Запускаю проект
python manage.py runserver
