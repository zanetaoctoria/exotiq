from django.urls import path
from main.views import edit_items
from main.views import delete_items
from main.views import login_user
from main.views import register
from main.views import logout_user
from main.views import show_main, create_items_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import add_items_entry_ajax


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_items_entry', create_items_entry, name='create_items_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('edit-items/<uuid:id>', edit_items, name='edit_items'),
    path('delete/<uuid:id>', delete_items, name='delete_items'), # sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-items-entry-ajax', add_items_entry_ajax, name='add_items_entry_ajax'),

]