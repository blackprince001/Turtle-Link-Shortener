# Turtle - A link shortener w/ FastAPI

Currently procrastinating the project.

Inspiration from [Real Python Website](https://realpython.com/build-a-python-url-shortener-with-fastapi/)

Link Shortener demo working on localhost!

<img src="/assets/demo-recording.gif">
</img>

> How user data is stored
![Alt text](assets/user-table.png)

> How shorted links by a specific user are mapped
![label](assets/user-created-urls.png)

> How shorted links are stored
![label](assets/url-created-records.png)

## Project Structure

```console
.
├── README.md
├── app.py
├── assets
│   └── link-shortener-demo.mp4
├── poetry.lock
├── pyproject.toml
├── routes
│   ├── __init__.py
│   ├── admin.py
│   └── user.py
├── schemas
│   ├── __init__.py
│   ├── url.py
│   ├── user.py
│   └── user_url.py
├── shortener.db
├── tests
│   └── __init__.py
├── turtle_link_shortener
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── errors.py
│   ├── models.py
│   └── security.py
└── utils
    ├── __init__.py
    ├── database_utils.py
    └── router_utils.py

7 directories, 23 files
```
