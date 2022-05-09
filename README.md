To run the project locally:
python -m apps.server

To call the API from postman:
http://localhost:5000/obj-creation
POST
BODY - (form-data):
{ file: <the file - test.png/test.jpg>, local_path: <the project local path (for example: C:/Users/Shachar/Desktop/Projects/hdProject)>}