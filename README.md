# glean-clone-backend

## Setting Up the Project

### Prerequisites

- Python 3.x installed on your system
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Installation

1. **Clone the Repository**

   First, clone the project repository to your local machine using Git:

   ```
   git clone https://your-repository-url.git
   cd your-project-directory
   ```

2. **Create and Activate a Virtual Environment (Optional)**

   It's a good practice to use a virtual environment for your Python projects. This keeps your project's dependencies
   separate from your system's Python environment.

   - **For macOS/Linux**:

     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **For Windows**:

     ```
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install Dependencies**

   Install all dependencies listed in `requirements.txt`:

   ```
   pip install -r requirements.txt
   ```

### Configure the Project

1. **Environment Variables**

   Ensure all necessary environment variables are set up. If your project uses a `.env` file for environment variables,
   make sure it's correctly configured according to your project's documentation.

2. **Run Migrations**

   Apply the Django database migrations to set up your database schema:

   ```
   python manage.py migrate
   ```

3. **Create a Django Superuser**

   Create an administrative user for accessing the Django admin site:

   ```
   python manage.py createsuperuser
   ```

   Follow the prompts to set up the superuser's username, email, and password.

### Running the Development Server

1. **Start the Django Development Server**

   Run the following command to start the Django development server:

   ```
   python manage.py runserver
   ```

2. **Access the Site**

   Open your web browser and go to [http://localhost:8000](http://localhost:8000) to view the project. To access the
   Django admin site, go to [http://localhost:8000/admin](http://localhost:8000/admin) and log in using your superuser
   credentials.

Congratulations! You've successfully set up and run your Django project locally.
