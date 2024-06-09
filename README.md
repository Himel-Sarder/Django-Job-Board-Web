# Django Job Board Webpage

## Table of Contents
- [Screenshots](#screenshots)
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Screenshots
Header
![image](https://github.com/Himel-Sarder/Django-Job-Board-Webpage/assets/143216886/11621625-bda4-4794-b433-10a5d86d3022)
Footer
![image](https://github.com/Himel-Sarder/Django-Job-Board-Webpage/assets/143216886/cdd895f0-4b61-45ad-bf8f-468532d92e1a)
Hover
![image](https://github.com/Himel-Sarder/Django-Job-Board-Webpage/assets/143216886/d6bf3982-73b3-48a7-bb5d-45dcc9db6ade)
Detail Page
![image](https://github.com/Himel-Sarder/Django-Job-Board-Webpage/assets/143216886/94e434fc-52c1-4c37-8881-aa52ac488c5c)
Dark Mode
![image](https://github.com/Himel-Sarder/Django-Job-Board-Webpage/assets/143216886/611da289-f7b9-4fc7-a19b-457c2834243d)
![image](https://github.com/Himel-Sarder/Django-Job-Board-Webpage/assets/143216886/79703059-2418-437c-be7c-2ce5e2d5c62c)

## Admin pannel Screenshot   
![image](https://github.com/Himel-Sarder/Django-Job-Board-Webpage/assets/143216886/c6dc69d7-5ada-4544-90c3-c3f69f0017f2)
![image](https://github.com/Himel-Sarder/Django-Job-Board-Webpage/assets/143216886/b6c6432d-db5a-4db7-aa90-c67a51ce577e)

## Project Overview
This project is a job board web application built with Django. Users can view job postings, see detailed information about each job, and toggle between light and dark themes. The site is styled with Tailwind CSS and includes features such as dynamic content rendering and theme persistence using local storage.

## Features
- View a list of job postings.
- See detailed information for each job.
- Toggle between light and dark mode themes.
- Responsive design using Tailwind CSS.
- Persistent dark mode preference using local storage.
- Clean and professional UI.

## Technologies Used
- Django
- Python
- HTML
- CSS (Tailwind CSS)
- JavaScript

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Himel-Sarder/Django-Job-Board-Webpage.git
   cd django-job-board
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Configuration
1. **Database configuration**: Edit the `DATABASES` setting in `settings.py` if you want to use a different database.
2. **Static files**: Ensure that Tailwind CSS is included and configured properly in your `settings.py`.

## Usage
- **Home Page**: Displays the list of job postings.
- **Job Details**: Click on any job posting to see detailed information about the job.
- **Dark Mode**: Use the "Toggle Dark Mode" button in the top right corner to switch between light and dark themes.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


