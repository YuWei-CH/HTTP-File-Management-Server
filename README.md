# flask-file-server

File server for Anubis Interview

## Prereq

### MySQL(or other SQL) + Flask(with Flask-SQLAlchemy and Flask-Migrate)

```bash
pip install Flask-SQLAlchemy Flask-Migrate
```

### Initial table with Migrate, table should be define in models.py

```bash
flask db init

flask db migrate -m "XXXX"

flask db upgrade

```

## Front End design

### It is the implementation of the front-end structure using HTML and Bootstrap. The front-end includes: upload function, list function and download function. list contains file name, file size and file date. Files are grouped according to file type (suffix).

## Back End design

### Use flask as the backend framework. Storing files into relational databases such as MySQL. Utilizing asynchrony to reduce server stress.

### API Design

1. Upload:  
    Route: /upload  
    Method: POST  
    Function: Receive the uploaded file and save it to the database.  
    Data Received: Use Flask's request object to get the uploaded file.
   <br />
   Identifier: 200 -> Success; 400 -> Error; 409 -> Duplicate file; 500 -> Failed;
2. List:  
    Route: /files  
    Method: Get  
    Function: Lists basic information about all files in the database.  
    Return: Return a list of files in JSON format.
   <br />
3. Download:  
    Route: /download/<file_id>  
    Method: GET  
    Function: Downloads files based on file ID.  
    Parameter: file_id - The unique identifier of the file to be downloaded.

## Database

### `file`

| Column Name | Data Type   | Constraints            |
| ----------- | ----------- | ---------------------- |
| id          | INT         | Primary Key, Auto-Incr |
| name        | VARCHAR     | Not Null               |
| size        | BIGINT      |                        |
| upload_date | DATETIME    |                        |
| mime_type   | VARCHAR     |                        |
| data        | LARGEBINARY |                        |
| hash        | VARCHAR     |                        |
