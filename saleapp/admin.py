from flask_admin import Admin, AdminIndexView, expose
from flask_admin.theme import Bootstrap4Theme
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from saleapp import app, db
from models import Category, Product



class MyCategoryView(ModelView):
    column_list = ['name', 'products']
    column_searchable_list = ['name']
    column_filters = ['name']
    column_labels = {
        "name": "Tên loại",
        "products":"Danh sách sản phẩm"
    }

    def is_accessible(self) -> bool:
        return current_user.is_authenticated


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self) -> str:
        return self.render('admin/index.html')

admin = Admin(app=app, name='E=COMMERCE', theme=Bootstrap4Theme(), index_view=MyAdminIndexView() )

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(ModelView(Product, db.session))


