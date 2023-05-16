from django.contrib.auth.base_user import BaseUserManager

class customuser(BaseUserManager):

    def create(self, email, password, **data):
        if not email:
            raise ValueError("Email Must Be Provided")
        
        email = self.normalize_email(email)

        user = self.model(email = email, **data)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, password, **data):
        data.setdefault("is_active", True)
        data.setdefault("is_superuser", True)
        data.setdefault("is_staff", True)

        if data.get('is_active') is not True:
            raise ValueError("is active status must be true")       
        if data.get('is_superuser') is not True:
            raise ValueError("is superuser status must be true")       
        if data.get('is_staff') is not True:
            raise ValueError("is staff status must be true")  

        return self.create(email=email, password=password, **data)     