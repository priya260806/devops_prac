# 1 open cmd
python --version
node --version
npm --version
"C:\Program Files\PostgreSQL\18\bin\psql.exe" --version 
netstat -ano | findstr :5433

# 2 create project folder
# open cmd
cd %USERPROFILE%\Desktop
# Then:
mkdir three-tier-student-app
# Then:
cd three-tier-student-app
# Now create the three tiers:
mkdir backend
mkdir frontend

# 3 Create the PostgreSQL database
# Open pgAdmin
# Go to:
Servers → PostgreSQL 18 → Databases
Right-click Databases → Create → Database
# Use:
Database: studentdb2
# Then click Save.

