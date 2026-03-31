from django.contrib import admin
from .models import *   # يجيب كل الموديلز

admin.site.register(CompanyBranch)
admin.site.register(Customer)
admin.site.register(Dept)
admin.site.register(EmpState)
admin.site.register(LoginEmp)
admin.site.register(Offers)
#admin.site.register(OffersPi)
admin.site.register(PersonalInfo)
admin.site.register(Product)
#admin.site.register(ProductBranch)
admin.site.register(Role)
admin.site.register(Storehouse)
#admin.site.register(StorehouseBranch)
#admin.site.register(StorehouseProduct)
admin.site.register(Users)