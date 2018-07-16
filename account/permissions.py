from rest_framework.authentication import  BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.authentication import BaseAuthentication
from utils.Exception import MyException
from django.contrib.auth import login
from rest_framework.request import Request
from account.models import User
from project.models import Project,ProjectInvestDataModel
from rest_framework import permissions
class MyBasicAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = getattr(request._request, 'user', None)
        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active:
            return None
            # CSRF passed with authenticated user
        return (user, None)




class IsAllowedToUse(BasePermission):
    modulepermissiontemplate = {
        "SWRY": {
                 "/Project/projects/is_altered/": ["PUT", ],
                 "/Project/projects/concludedpro_apply/": ["GET", "POST"],
                 "/Project/projects/": ["POST","GET","DELETE"],
                 "/Project/fundapplys/is_altered/": ["PUT", ],
                 "/Project/fundapplys/": ["GET","POST","DELETE" ],
                 "/Project/refundapplys/is_altered/": ["PUT", ],
                 "/Project/refundapplys/": ["GET","POST","DELETE"],
                 "/Project/invoiceapplys/is_altered/":["PUT",],
                 "/Project/invoiceapplys/": ["GET","POST" ,"DELETE"],
                 "/statis/day/":["GET"],
                 "/statis/project_day/":["GET"],
                 "/statis/user_day/": ["GET"],
                 "/statis/user/": ["GET"],
                 "/statis/all/": ["GET"],
                 "/Project/projectinvestdata/": ["GET"],
                 "/Project/projectinvestdata/export_investdata_excel/": ["GET"],
                 "/Project/projectinvestdata/import_audit_projectdata_excel/": ["POST"],
                 "/Project/projectinvestdata/import_audit_projectdata_excel_except/": ["POST"],
                 "/Project/projectinvestdata/import_projectdata_excel/": ["POST"],
                 "/Project/operatorlogdetail/":["GET"]

        },
        "SHRY": {
                "/Project/projects/concludedpro_rejected/": ["POST"],
                "/Project/projects/concludedpro_approved/": ["POST"],
                "/Project/projects/lanchedpro_rejected/": ["POST"],
                "/Project/projects/lanchedpro_approved/": ["POST"],
                "/Project/projects/": ["GET"],
                "/Project/fundapplys/apply_approved/": ["POST"],
                "/Project/fundapplys/apply_rejected/": ["POST"],
                "/Project/fundapplys/": ["GET"],
                "/Project/refundapplys/apply_approved/": ["POST", ],
                "/Project/refundapplys/apply_rejected/": ["POST"],
                "/Project/refundapplys/": ["GET"],
                "/Project/invoiceapplys/apply_approved/": ["POST", ],
                "/Project/invoiceapplys/apply_rejected/": ["POST"],
                "/Project/invoiceapplys/": ["GET"],
                "/statis/day/": ["GET"],
                "/statis/project_day/": ["GET"],
                "/statis/user_day/": ["GET"],
                "/statis/user/": ["GET"],
                "/statis/all/": ["GET"],
                "/Project/operatorlogdetail/": ["GET"]

        }
        ,
        "SJRY": {
                "/Project/projects/": ["GET"],
                "/statis/day/": ["GET"],
                "/statis/project_day/": ["GET"],
                "/statis/user_day/": ["GET"],
                "/statis/user/": ["GET"],
                "/statis/all/": ["GET"],
                "/Project/projectinvestdata/": ["GET"],
                "/Project/projectinvestdata/export_investdata_excel/": ["GET"],
                "/Project/projectinvestdata/import_audit_projectdata_excel/": ["POST"],
                "/Project/projectinvestdata/import_audit_projectdata_excel_except/": ["POST"],
                "/Project/projectinvestdata/import_projectdata_excel/": ["POST"],
                "/Project/operatorlogdetail/":["GET"]
        },
        "CWRY":{
                "/Project/fundapplys/apply_approved/": ["POST"],
                "/Project/fundapplys/apply_rejected/": ["POST"],
                "/Project/fundapplys/": ["GET"],
                "/Project/refundapplys/apply_approved/": ["POST", ],
                "/Project/refundapplys/apply_rejected/": ["POST"],
                "/Project/refundapplys/": ["GET"],
                "/Project/invoiceapplys/apply_approved/": ["POST", ],
                "/Project/invoiceapplys/apply_rejected/": ["POST"],
                "/Project/invoiceapplys/": ["GET"],
                "/statis/day/": ["GET"],
                "/statis/project_day/": ["GET"],
                "/statis/user_day/": ["GET"],
                "/statis/user/": ["GET"],
                "/statis/all/": ["GET"]
        }

    }


    def has_permission(self, request,view):
        """该类权限的意义在于对执行方法的权限的控制，而非权限的具体内容
        在 permission_class 中 ，首先 self.get_view_name() 获取当前 view 的名称，然后 self.get_method()获取当前方法，然后
        获取对应用户的 permission_record ，如果 record 的集合 中有对应的 view 和方法,就判定通过
        但是权限管理人员添加权限的话，是添加的组合权限， 后台先将组合模板（就是对应 view 和方法）列出来，管理人员添加的是模板
        模板就是权限的组合"""
        current_user, current_method, current_resource = request.user, request.method,request.path
        x = request.path.split('/')
        x= [ i for i in x if i.isdigit()==False][1:-1]
        # y = "/Project/projects/".split('/')[1:-1]
        pmatch = lambda x,y: all(True if i in x else False for i in y)
        if current_user.is_anonymous == True or current_user.is_authenticated == False:
            return False
        if current_user.is_superuser == True:
            return True


        aimuser = User.objects.filter(uid=current_user.uid)
        if aimuser.exists():
            umodulespems = aimuser[0].upermission.all()
            if umodulespems.exists():
                moduletemplatepermission = self.modulepermissiontemplate
                result = any(True \
                                 if  pmatch(x,j.split('/')[1:-1]) \
                                    and current_method in moduletemplatepermission[i.desc][j] \
                                 else False \
                             for i in umodulespems for j in moduletemplatepermission[i.desc])
            else:
                return False
            return result

        return False

    # def has_permission(self, request,view):
    #     """该类权限的意义在于对执行方法的权限的控制，而非权限的具体内容
    #     在 permission_class 中 ，首先 self.get_view_name() 获取当前 view 的名称，然后 self.get_method()获取当前方法，然后
    #     获取对应用户的 permission_record ，如果 record 的集合 中有对应的 view 和方法,就判定通过
    #     但是权限管理人员添加权限的话，是添加的组合权限， 后台先将组合模板（就是对应 view 和方法）列出来，管理人员添加的是模板
    #     模板就是权限的组合"""
    #     current_user, current_method, current_resource = request.user, request.method,request.path
    #     print(view.action)
    #     print(dir(view.action))
    #     print(request.path)
    #     x = request.path.split('/')
    #     x= [ i for i in x if i.isdigit]
    #     filter(func1,x)
    #     del_x = filter(str.isdigit, x)
    #     for i in del_x:
    #         x.remove(i)
    #     y = "/Project/projects/is_altered".split('/')
    #     pmatch = lambda x,y: all(True if i in x  else False for i in y)
    #     #request.path,action,detailed
    #     #request.path  view.action
    #     print(current_resource, current_method, current_user)
    #     if current_user.is_anonymous == True or current_user.is_authenticated == False:
    #         return False
    #     # if current_user.is_superuser == True:
    #     #     return True
    #     # if current_user.is_staff ==True :
    #     #pmatch=lambda x:request.path+request.action match j
    #     # j="projects|is_altered"
    #     # x=j.split('|')
    #     # pmatch = lambda x,y,z : all(True if i in current_resource or view.action else False for i in x)
    #     # result=pmatch(x,current_resource,view.action)
    #     # print(result)
    #     # if x[0] in current_resource
    #     # if x[1] in view.action return
    #
    #     aimuser = User.objects.filter(uid=current_user.uid)
    #     print(aimuser)
    #     if aimuser.exists():
    #         umodulespems = aimuser[0].upermission.all()
    #         if umodulespems.exists():
    #             moduletemplatepermission = self.modulepermissiontemplate
    #             result = any(True \
    #                              if  pmatch(j.split('|'),current_resource,view.action) \
    #                                 and current_method in moduletemplatepermission[i.desc][j] \
    #                              else False \
    #                          for i in umodulespems for j in moduletemplatepermission[i.desc])
    #         else:
    #             return False
    #         return result
    #
    #     return False



class MyBasicAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = getattr(request._request, 'user', None)
        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active:
            return None
            # CSRF passed with authenticated user
        return (user, None)


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        #         if request.method in permissions.SAFE_METHODS:
        #             return True

        # 写的请求只对对象的创建者开放
        if not request.user.is_authenticated:
            return False
        return request.user.is_superuser


class IsOwnerOrStaff(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if isinstance(obj,Project):
            return request.user.is_superuser or obj.contact == request.user
        else:
            return request.user.is_superuser or obj.apply_man == request.user


# class IsOwnerOrStaffOrSDRY(permissions.BasePermission):
#     """
#     Object-level permission to only allow owners of an object to edit it.
#     Assumes the model instance has an `owner` attribute.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         # if obj 是activity的话，那么有or的apullman=request.user
#         # 如果是   shopcontact的话，那么就没有apullman
#         if isinstance(obj, Activity):
#             if not request.user.is_authenticated:
#                 return False
#             return request.user.is_staff or obj.user == request.user or request.user.is_sdry() or obj.apullman == request.user
#         if isinstance(obj, Shopcontact):
#             if not request.user.is_authenticated:
#                 return False
#             return request.user.is_staff or obj.user == request.user or request.user.is_sdry()
