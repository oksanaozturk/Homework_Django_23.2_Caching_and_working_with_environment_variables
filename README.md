# Homework_Django_23.1_Access_rights (Права доступа)
# Это продолжение Homework_Django_22.2_Authentication

# Для разворачивания проекта потребуется создать и заполнить файл .env  по шаблону файла .env.sample

* Задание 1
Создайте группу для роли модератора и опишите необходимые доступы:

- может отменять публикацию продукта,
- может менять описание любого продукта,
- может менять категорию любого продукта.

*Задание 2
Реализуйте решение, которое проверит, что редактирование продукта доступно только его владельцу.

* Рекомендации от Наставника:
  Ты также можешь проверять принадлженость к группе в контролере используя userPassesTestMixin

Пример

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def is_manager(user):
    return user.groups.filter(name='Managers').exists()



class MyView(LoginRequiredMixin, UserPassesTestMixin, View):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
	        return is_manager(self.request.user)
