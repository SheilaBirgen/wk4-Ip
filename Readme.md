# Personal Blog

## Author
Sheila Birgen Jerono

## Technologies used
    -python
    -pip
    -html
    -css
    -flask

## Installation
To get the code..

1. Cloning the repository:

```bash
https://github.com/SheilaBirgen/ip4
```

2. Move to the folder and install requirements

```bash
cd ip4
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application

```bash
python3.6 manage.py server
```

Open the application on your browser `127.0.0.1:5000`.

## Description
A blog post is app that allows a user to post what is in their mind,comment and delete on other people's post 

## BDD
| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           | Select between signup and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app pitches based on categories and commenting section |
| Select comment button |             **Comment**             |             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments tamplate with your comment and other comments |