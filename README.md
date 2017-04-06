# README

Putting together the login, registration and password reset tutorials from https://simpleisbetterthancomplex.com into one repository.

Login
- https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html

Registration
- https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

Password Reset
- https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html

**Notes**
- I have added a stylesheet auth_style.css to enable styling to be done.
- There are settings files for production and development, both importing from a base set of settings.
- Emails in development appear in the console as we have set EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' in the dev.py settings file.

**Improvements that could be made**
- At the moment the password reset is done by email address, which doesn't have to be unique among users.