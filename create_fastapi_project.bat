@echo off

:: Create main directories
mkdir app
mkdir app\api
mkdir app\core
mkdir app\db
mkdir app\models
mkdir app\schemas
mkdir tests

:: Create main files
echo. > main.py
echo. > requirements.txt

:: Create app files
echo. > app\__init__.py
echo. > app\api\__init__.py
echo. > app\api\endpoints.py
echo. > app\core\__init__.py
echo. > app\core\config.py
echo. > app\db\__init__.py
echo. > app\db\base.py
echo. > app\models\__init__.py
echo. > app\schemas\__init__.py

:: Create test files
echo. > tests\__init__.py
echo. > tests\test_api.py

:: Create .env files
echo DATABASE_URL=sqlite:// > .env
echo DATABASE_URL=postgresql://user:password@localhost/dbname > .env.production

echo FastAPI project structure created successfully!