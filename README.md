# flask-file-server
File server for Anubis Interview

## Prereq

### MySQL(or other SQL) + Flask(with Flask-SQLAlchemy and Flask-Migrate) 
```bash
pip install Flask-SQLAlchemy Flask-Migrate
``` 

### Initial table with Migrate,  table should be define in models.py   
```bash
flask db init

flask db migrate -m "XXXX"

flask db upgrade

```

## Database
### `file`

| Column Name  | Data Type | Constraints            |
| ------------ | --------- | ---------------------- |
| id           | INT       | Primary Key, Auto-Incr |
| name         | VARCHAR   | Not Null               |
| size         | BIGINT    |                        |
| upload_date  | DATETIME  |                        |
| mime_type    | VARCHAR   |                        |
| data         | LARGEBINARY |                      |


