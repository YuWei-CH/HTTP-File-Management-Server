# flask-file-server

File server

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

### Use flask as the backend framework. Storing files into relational databases such as MySQL. Utilizing AJAX for asynchronous communication reduces server load and enhances efficiency.

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
    Function: Lists basic information about all files in the database or list or list the files that match the criteria.  
    Return: Return a list of files in JSON format.
   <br />
3. Download:  
   Route: /download/<file_id>  
   Method: GET  
   Function: Downloads files based on file ID.  
   Parameter: file_id - The unique identifier of the file to be downloaded.
   <br />
4. Delete:  
   Route: /delete/<file_id>  
   Method: DELETE  
   Function: delete files based on file ID.  
   Parameter: file_id - The unique identifier of the file to be deleted.

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

## TODO:

### Backend Processing Enhancement

Text Analysis Integration:  
Implement text analysis features for processing and analyzing textual data. This might include sentiment analysis, text classification, or natural language processing tasks.

Image Processing Capabilities:  
Add image processing features, such as image resizing, filtering, or advanced image manipulations, possibly using libraries like PIL (Python Imaging Library) or OpenCV.

### Storage and Scalability

Switch to Amazon S3 for Object-Based Storage:  
Migrate the current storage system to Amazon S3 to leverage its scalability, security, and reliability for object storage. This will involve integrating the AWS SDK and modifying the file handling logic.

### Dockerization for Microservices Architecture:

Containerize the application using Docker to facilitate a microservices architecture. This includes creating Dockerfiles, setting up Docker Compose for local development, and potentially orchestrating with Kubernetes for larger deployments.

### High-Concurrency and Performance Optimization

Incorporate Message Queues (MQ):  
Implement message queues to handle high-load, asynchronous tasks, and improve the application's ability to handle large volumes of requests. Technologies like RabbitMQ or Kafka could be used.

Integrate Redis for Caching and Session Storage:  
Utilize Redis for fast, in-memory data storage to enhance the performance of the application. This could be particularly useful for caching frequently accessed data and managing user sessions in a distributed environment.
