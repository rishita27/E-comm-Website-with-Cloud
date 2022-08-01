from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class MyUserManager(BaseUserManager):
    def create_user(self,full_name,phonenumber,email,password=None,admin=False,email_verify=False,active=True,referral_code=None,referred_by=None):
        if not full_name:
            raise ValueError(_("Please Enter Full Name !."))
        if not phonenumber:
            raise ValueError(_("Please Enter Mobile Number !."))
        if not email:
            raise ValueError(_("Please Enter Email !."))
        if not password:
            raise ValueError(_("Please Enter Password !."))
        user=self.model(email=self.normalize_email(email),
                        full_name=full_name,
                        phonenumber=phonenumber,
                        admin=admin,
                        active=active,
                        email_verify=email_verify,
                        referral_code=referral_code,
                        referred_by=referred_by
                        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,full_name,phonenumber,email,password=None,admin=True,email_verify=False,active=True,referral_code=None,referred_by=None):
        user=self.create_user(full_name,phonenumber,email,password,admin,email_verify,active,referred_by,referral_code)
        user.save(using=self._db)
        return user


