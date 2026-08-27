@echo off
echo ==========================================
echo MOE HR SYSTEM - LANDING PAGE DEPLOYMENT
echo ==========================================

echo Creating deployment package...
mkdir deploy 2>nul
copy index.html deploy\
copy styles.css deploy\
copy favicon.ico deploy\

echo Deployment package created in 'deploy' folder
echo ==========================================
echo To deploy:
echo 1. Upload the 'deploy' folder to your web server
echo 2. Or run: node server.js
echo ==========================================
pause