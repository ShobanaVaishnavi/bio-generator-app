# Bio Generator Project

## Overview

This is a simple web application built using **Flask** that generates bios based on user-selected traits, careers, and interests. The application allows users to select from predefined categories and generate a personalized bio. It’s a fun tool that can be used to quickly create bios for people with different characteristics and preferences.

### Purpose

This project was created as a learning exercise to practice web development and Flask. Additionally, it is part of an **internship assessment** I received from **WolfPack**, which I worked on to demonstrate my ability to develop a simple, functional web application. The goal was to understand how to create a basic Flask web app with form handling, template rendering, and validations.

## Features

- **Career selection**: Choose from various career options.
- **Interest selection**: Select an interest or hobby.
- **Trait selection**: Pick a personal trait.
- **Randomized Bio Generation**: Based on your choices, a bio is randomly generated from a set of predefined templates.
- **Form Validation**: Ensures that all fields are selected before submission.
- **Simple, user-friendly interface** for easy navigation and bio creation.


## Technologies Used
- **Python 3.x**
- **Flask** (for web framework)
- **HTML/CSS** (for front-end)
- **Jinja2 templating** (used in Flask to dynamically render HTML pages)
- **Git** for version control
- **GitHub** for code hosting


## Installation

### Prerequisites
To run this project, you'll need:
- Python 3.x installed on your machine.
- pip (Python package installer).

### Setup
Follow these steps to set up this on your local machine:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ShobanaVaishnavi/bio-generator-app.git
    cd bio-generator
    ```

2. **Set up environment variables**:
    Create a **`.env` file** and add a secret key:
    ```bash
    SECRET_KEY=your_secret_key
    ```

3. **Run the Flask application**:
    ```bash
    python app.py
    ```

    The app should now be running at `http://127.0.0.1:5000/`.

## How to Use
1. Open the web application in your browser by navigating to **`http://127.0.0.1:5000/`**.
2. From the homepage, select a career, interest, and trait from the dropdown menus.
3. Click **"Generate Bio"** to see a customized bio based on your selections.
4. If any field is left blank, the application will prompt you to fill in all fields before proceeding.


## Screenshots
Below are the screenshots of the Bio Generator web application:

![Home Page](screenshots\home_page.png)
![Selected Page](screenshots\selected.png)
![Generated Bio Page](screenshots\result_page.png)

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request with your changes.

## Acknowledgments
- Thanks to [WolfPack](https://wolfpackdigi.com) for the opportunity to work on this project as part of their internship assessment.

## License
This project is open-source and available under the MIT License.  - see the [LICENSE](LICENSE) file for details.