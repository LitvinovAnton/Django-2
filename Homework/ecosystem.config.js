module.exports = {
  apps : [{
    name: 'django_server',
    script: 'manage.py',
    cron_restart: '0 * * * *', // автоматический рестарт каждый час
    args: 'runserver 0.0.0.0:8000',
    interpreter: 'python3',
    env: {
      "DJANGO_SETTINGS_MODULE": "homework_project.settings",
      "PYTHONUNBUFFERED": "1",
    }
  }]
};


//{
//    script: "python3",
//    args: ["manage.py", "runserver", "0.0.0.0:8000"],
//    name: "django-server"
//}


//const { exec } = require('child_process');
//
//exec('pm2 start python3 manage.py runserver --name "django-server" -- 0.0.0.0:8000', (error, stdout, stderr) => {
//  if (error) {
//    console.error(`Error starting Django: ${error}`);
//    return;
//  }
//  console.log(`Django started: ${stdout}`);
//});