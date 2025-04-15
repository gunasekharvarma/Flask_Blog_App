# Flask Blog App

A feature-rich blogging application built with Flask, allowing users to create accounts, publish posts, comment, and more.

## Features

- **User Authentication**
  - Register new accounts
  - Login/Logout functionality
  - Password reset via email
  - Profile management

- **Blog Posts**
  - Create, read, update, and delete posts
  - Rich text formatting
  - Image uploads for posts
  - Post categorization



## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Forms**: Flask-WTF
- **Email**: Flask-Mail
- **Image Processing**: Pillow

## Installation

### Prerequisites

- Python 3.6+
- pip (Python package manager)
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/gunasekharvarma/Flask_Blog_App.git
   cd Flask_Blog_App
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # On Windows
   set FLASK_APP=run.py
   set FLASK_ENV=development
   set SECRET_KEY=your_secret_key
   set MAIL_USERNAME=your_email@gmail.com
   set MAIL_PASSWORD=your_email_password
   
   # On macOS/Linux
   export FLASK_APP=run.py
   export FLASK_ENV=development
   export SECRET_KEY=your_secret_key
   export MAIL_USERNAME=your_email@gmail.com
   export MAIL_PASSWORD=your_email_password
   ```

5. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Usage

1. Start the development server:
   ```bash
   flask run
   ```

2. Open your browser and navigate to `http://localhost:5000`

3. Register a new account to start using the application



## API Endpoints

### Authentication

- `POST /register` - Register a new user
- `POST /login` - Authenticate user and create session
- `GET /logout` - End user session

### Posts

- `GET /posts` - Get all posts
- `GET /posts/<post_id>` - Get a specific post
- `POST /posts/new` - Create a new post
- `PUT /posts/<post_id>/update` - Update a post
- `DELETE /posts/<post_id>/delete` - Delete a post

### Users

- `GET /user/<username>` - View user profile
- `PUT /account` - Update user profile


## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request



