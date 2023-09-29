**Yatube - блог для публикации постов**

Yatube - это веб-приложение, которое позволяет пользователям публиковать свои посты, комментировать их, подписываться на интересующих авторов и объединяться в группы по интересам.

---
### Технический стек
![Python](https://img.shields.io/badge/-Python-386e9d?style=flat&logo=Python&logoColor=ffd241&)
![Django](https://img.shields.io/badge/-Django-0aad48?style=flat&logo=Django)
![Django Rest Framework](https://img.shields.io/badge/DRF-red?style=flat&logo=Django)

---
### **Описание**

Yatube решает задачу обмена мнениями и опытом между пользователями. Каждый зарегистрированный пользователь может:
- Публиковать свои посты;
- Комментировать посты;
- Подписываться на других авторов;

---

### **Установка**

Для локального развертывания проекта Yatube выполните следующие шаги:

1. Клонируйте репозиторий:
```
git clone ссылка_на_репозиторий
```

2. Установите необходимые зависимости:
```
pip install -r requirements.txt
```

3. Произведите миграции:
```
python manage.py migrate
```

4. Запустите сервер:
```
python manage.py runserver
```

---

### **Примеры запросов к API**

1. **Получение всех постов:**
```
GET /v1/posts/
```

2. **Публикация нового поста:**
```
POST /v1/posts/
{
    "text": "Текст вашего поста",
    "group": id_группы
}
```

3. **Получение комментариев к посту:**
```
GET /v1/posts/{post_id}/comments/
```

4. **Добавление комментария к посту:**
```
POST /v1/posts/{post_id}/comments/
{
    "text": "Текст вашего комментария"
}
```

5. **Подписаться на пользователя:**
```
POST /v1/follow/
{
    "following": "username_пользователя"
}
```

---

Для детальной информации об API и его возможностях обратитесь к документации по **projecthost/redoc**

---
Автор - **Шулькин Николай** <a href="https://www.github.com/stanlyzera" target="_blank" rel="noreferrer"> <picture> <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github-dark.svg" /> <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github.svg" /> <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github.svg" width="32" height="32" /> </picture> </a>

