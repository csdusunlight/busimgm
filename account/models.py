#coding:utf-8
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin
# Create your models here.
class Group(models.Model):

    gname = models.CharField('分组名',max_length=10, unique=True)
    def __str__(self):
        return self.gname
    class Meta:
        verbose_name = '分组'
        verbose_name_plural = '分组'

class Permission(models.Model):
    #增加对应方法字段表示具体哪个视图的方法
    desc = models.CharField("权限码", max_length=60)
    modulename = models.CharField("功能模块", max_length=60, primary_key=True)
    def __str__(self):
        return self.desc+self.modulename
    class Meta:
        verbose_name = '权限'
        verbose_name_plural = '权限'


class MyUserManager(BaseUserManager):

    def _create_user(self, uid,uname,uqq,password,
                     is_staff, is_superuser):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = datetime.datetime.now()
        if not uid or not uname or not uqq :
            raise ValueError('The given qq, mobile and username must be set')
        user = self.model(uid=uid,uname=uname,uqq=uqq,
                          is_staff=is_staff,
                          is_active=True, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, uid,uname,uqq, password=None, **extra_fields):
        return self._create_user(uid,uname,uqq,password, False, False)

    def create_superuser(self, uid,uname,uqq, password):
        return self._create_user(uid,uname,uqq,password, True, True)

class User(AbstractBaseUser,PermissionsMixin):

    uid =models.CharField("用户手机号", max_length=11, unique=True)
    uname = models.CharField("用户名字",max_length=10, unique=True)
    ugroup = models.ForeignKey(Group,on_delete=models.SET_NULL,null=True,verbose_name="用户组")
    upermission = models.ManyToManyField(Permission,verbose_name="权限设置")
    uqq1 = models.CharField("QQ号", max_length=15)
    uqq = models.CharField("QQ号", max_length=20)
    #picture = models.ImageField(upload_to='photos/user_headphoto', verbose_name=u"个人头像")
  # uaddtime = models.DateTimeField(default=timezone.now)
    ujointime = models.DateTimeField('注册时间', default=timezone.now)
    uleavetime = models.DateTimeField('离职时间', null=True, blank=True)
    uremarks = models.CharField('用户管理备注',max_length=50,blank=True)
    urecord = models.TextField('绩效管理备注',max_length=200,blank=True)
    is_staff = models.BooleanField('是否管理员', default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('是否可以登录', default=True,
                                    help_text=('Designates whether this user should be treated as '
                                               'active. Unselect this instead of deleting accounts.'))
    is_superuser = models.BooleanField(
        default=False,
        help_text=(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    project_new = models.IntegerField('新项目数',default=0)
    FundApplyLog_new = models.IntegerField('新项目数',default=0)
    RefundApplyLog_new = models.IntegerField('新项目数',default=0)
    InvoiceApplyLog_new = models.IntegerField('新项目数',default=0)
    USERNAME_FIELD = 'uid'
    objects = MyUserManager()
    REQUIRED_FIELDS = ['uname','uqq']
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

#class UserLog(models):
    def get_permission(self):
        userper =  self.upermission.all()
        userper = [i.desc for i in userper ]
        if self.is_staff :
            userper.append('STAFF')
        return userper

