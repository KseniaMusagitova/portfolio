# Portfolio Website

## Description

This is a personal portfolio project built with Django. The website displays information about me as a Python developer, my skills, projects and has a contact form for communication.

## Features

Profile display with brief information about the owner.
"About Me" section with detailed professional background.
"My Skills" section listing programming languages, frameworks, tools, and libraries.
"Projects" section showcasing completed projects with descriptions and links.
Contact form for sending messages.

## Installation and Setup
Clone the repository
```bash
git clone https://github.com/YourUsername/portfolio.git
cd portfolio
```

Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies
```bash
pip install -r requirements.txt
```

Apply migrations
```bash
python manage.py migrate
```

Create a superuser
```bash
python manage.py createsuperuser
```

Run the development server
```bash
python manage.py runserver
```

## Usage

Open your browser and go to http://127.0.0.1:8000 to view the website.
Go to http://127.0.0.1:8000/admin and log in with the superuser account to manage the website content.

## Data Models

Project
Field	Type	Description
title	CharField	Project title
description	RichTextField	Project description
link	URLField	Link to the project
Contact
Field	Type	Description
email	EmailField	Email address
name	CharField	Name of the sender
message	TextField	Message content

## Contribution

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature-name).
3. Make your changes and commit them (git commit -m 'Add some feature').
4. Push the branch (git push origin feature/your-feature-name).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
