# Django Authentication & User Management System

This project provides a comprehensive authentication and user management system using Django. It incorporates custom user models, JWT-based authentication, OAuth2 integration, role-based access control, and is containerized with Docker for deployment.

## Table of Contents
1. Project Setup
2. Custom User Model with Email Authentication
3. JWT-Based Authentication for API Access
4. OAuth2 Integration with Google/GitHub Login
5. Role-Based Access Control (RBAC)
6. API Endpoints for User Management
7. Testing and Security Enhancements
8. Deployment with Docker and Nginx
9. Documentation and Additional Resources

---

## 1. Project Setup

Begin by setting up the development environment and installing necessary dependencies.

### Steps:
- **Create a Virtual Environment**:
  A virtual environment isolates your Python dependencies for the project. This ensures that your project uses specific versions of libraries without affecting other projects.
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
  ```

- **Install Dependencies**:
  ```bash
  pip install django djangorestframework psycopg2-binary \
              djangorestframework-simplejwt django-allauth dj-rest-auth
  ```

- **Initialize Django Project and App**:
  ```bash
  django-admin startproject auth_system .
  python manage.py startapp users
  ```

- **Configure PostgreSQL Database**:
  Update `auth_system/settings.py` with PostgreSQL settings:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'your_db_name',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

Ensure PostgreSQL is installed and the database is created.

### References:
- Django: Setting Up a Django Development Environment
- Django: Databases

---

## 2. Custom User Model with Email Authentication

Replace Django’s default user model to use email as the unique identifier.

### Steps:
- **Define Custom User Model**:
  In `users/models.py`:
  ```python
  from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
  from django.db import models

  class CustomUserManager(BaseUserManager):
      def create_user(self, email, password=None, **extra_fields):
          if not email:
              raise ValueError('The Email field must be set')
          email = self.normalize_email(email)
          user = self.model(email=email, **extra_fields)
          user.set_password(password)
          user.save(using=self._db)
          return user

      def create_superuser(self, email, password=None, **extra_fields):
          extra_fields.setdefault('is_staff', True)
          extra_fields.setdefault('is_superuser', True)
          return self.create_user(email, password, **extra_fields)

  class CustomUser(AbstractBaseUser, PermissionsMixin):
      email = models.EmailField(unique=True)
      is_active = models.BooleanField(default=True)
      is_staff = models.BooleanField(default=False)

      objects = CustomUserManager()

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = []
  ```

- **Update Settings**:
  In `auth_system/settings.py`:
  ```python
  AUTH_USER_MODEL = 'users.CustomUser'
  ```

- **Apply Migrations**:
  ```bash
  python manage.py makemigrations users
  python manage.py migrate
  ```

### References:
- Django: Customizing Authentication

---

## 3. JWT-Based Authentication for API Access

Implement JSON Web Token (JWT) authentication for securing API endpoints.

### Steps:
- **Install Required Packages**:
  ```bash
  pip install djangorestframework-simplejwt
  ```

- **Configure REST Framework**:
  In `auth_system/settings.py`:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework_simplejwt.authentication.JWTAuthentication',
      ),
  }
  ```

- **Set Up Token Endpoints**:
  In `auth_system/urls.py`:
  ```python
  from django.urls import path
  from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

  urlpatterns = [
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      # Other URLs
  ]
  ```

### References:
- Django REST Framework: JWT Authentication

---

## 4. OAuth2 Integration with Google/GitHub Login

Enable social authentication using OAuth2 with providers like Google and GitHub.

### Steps:
- **Install Required Packages**:
  ```bash
  pip install django-allauth dj-rest-auth
  ```

- **Update Installed Apps**:
  In `auth_system/settings.py`:
  ```python
  INSTALLED_APPS += [
      'allauth',
      'allauth.account',
      'allauth.socialaccount',
      'allauth.socialaccount.providers.google',
      'allauth.socialaccount.providers.github',
      'dj_rest_auth',
      'dj_rest_auth.registration',
  ]
  ```

- **Configure Authentication Backends**:
  ```python
  AUTHENTICATION_BACKENDS = (
      'django.contrib.auth.backends.ModelBackend',
      'allauth.account.auth_backends.AuthenticationBackend',
  )
  ```

- **Set Up URLs**:
  In `auth_system/urls.py`:
  ```python
  from django.urls import path, include

  urlpatterns = [
      path('auth/', include('dj_rest_auth.urls')),
      path('auth/registration/', include('dj_rest_auth.registration.urls')),
      path('auth/social/', include('allauth.urls')),
      # Other URLs
  ]
  ```

- **Configure OAuth Providers**:
  Add your OAuth credentials in the Django admin interface under Social Applications.

### References:
- django-allauth: Installation
- dj-rest-auth: Installation

---

## 5. Role-Based Access Control (RBAC)

RBAC allows you to control access to different parts of the application based on user roles. This is achieved by assigning users to groups and granting permissions to those groups.

### Steps:
1. **Define Groups and Permissions**:
   - Use Django Admin:
     - Navigate to the Django Admin interface (`/admin`).
     - Under the "Auth" section, create groups such as `Admin`, `Moderator`, and `User`.
     - Assign permissions to these groups based on the actions they are allowed to perform (e.g., add, change, delete, view).
   - Programmatically:
     - You can define groups and permissions in your `models.py` or a custom management command. For example:
       ```python
       from django.contrib.auth.models import Group, Permission
       from django.contrib.contenttypes.models import ContentType
       from myapp.models import MyModel

       # Create a group
       admin_group, created = Group.objects.get_or_create(name='Admin')

       # Assign permissions to the group
       content_type = ContentType.objects.get_for_model(MyModel)
       permission = Permission.objects.get(
           codename='can_view_dashboard',
           content_type=content_type,
       )
       admin_group.permissions.add(permission)
       ```

2. **Assign Users to Groups**:
   - Use Django Admin:
     - Navigate to the "Users" section in the Django Admin interface.
     - Edit a user and assign them to one or more groups.
   - Programmatically:
     - Assign users to groups in your code:
       ```python
       from django.contrib.auth.models import Group
       from django.contrib.auth import get_user_model

       User = get_user_model()
       user = User.objects.get(email='user@example.com')
       admin_group = Group.objects.get(name='Admin')
       user.groups.add(admin_group)
       ```

3. **Check Permissions in Views**:
   - Use Django’s built-in `@permission_required` decorator to restrict access to views:
     ```python
     from django.contrib.auth.decorators import permission_required

     @permission_required('myapp.can_view_dashboard', raise_exception=True)
     def my_view(request):
         # Your view logic here
         pass
     ```
   - Alternatively, use `user.has_perm()` to check permissions programmatically:
     ```python
     if request.user.has_perm('myapp.can_view_dashboard'):
         # Allow access
         pass
     else:
         # Deny access
         pass
     ```

4. **Combine RBAC with Custom Decorators**:
   - Create custom decorators for more fine-grained access control:
     ```python
     from functools import wraps
     from django.http import HttpResponseForbidden

     def group_required(group_name):
         def decorator(view_func):
             @wraps(view_func)
             def _wrapped_view(request, *args, **kwargs):
                 if request.user.groups.filter(name=group_name).exists():
                     return view_func(request, *args, **kwargs)
                 return HttpResponseForbidden("You do not have access to this page.")
             return _wrapped_view
         return decorator

     @group_required('Admin')
     def admin_dashboard(request):
         # Admin-only view logic
         pass
     ```

### Additional Notes:
- Use Django’s built-in permissions framework to manage access control efficiently.
- Combine RBAC with middleware or custom decorators for more advanced use cases.
- Always test your RBAC implementation to ensure users only have access to the resources they are authorized to view or modify.

### References:
- [Django: Permissions and Authorization](https://docs.djangoproject.com/en/stable/topics/auth/default/#permissions-and-authorization)
- [Django: Groups](https://docs.djangoproject.com/en/stable/topics/auth/default/#groups)