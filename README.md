
### Running FastAPI:

1. **Clone the Repository:**
   ```shell
   git clone https://github.com/your-username/repo-name.git
   cd repo-name
   ```

2. **Install Dependencies:**
   ```shell
   pip install -r requirements.txt
   ```

3. **Set Environment Variables:**
   Create a `.env` file in the root directory and configure your environment variables, including database connection details and API tokens.

4. **Run FastAPI:**
   ```shell
   uvicorn main:app --reload
   ```
   The API will be accessible at `http://localhost:8000`.

### Setting Up PostgreSQL:

1. **Install PostgreSQL:**
   Follow the instructions on the [official PostgreSQL website](https://www.postgresql.org/download/) to install PostgreSQL on your system.

2. **Create Database:**
   ```shell
   createdb social_media_db
   ```

3. **Run Database Migrations:**
   ```shell
   alembic upgrade head
   ```
   This will apply the necessary database migrations.

4. **Configure Database URL:**
   Update the `.env` file with your PostgreSQL database URL:
   ```
   DATABASE_URL=postgresql://username:password@localhost/social_media_db
   ```
