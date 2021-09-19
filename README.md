# easy_drf_django

<!-- Creating db instance python  -->
python manage.py makemigrations

<!-- Migrating the db instance on db -->
python manage.py migrate

<!-- Navigate to ORM -->
cd checklist
python manage.py shell
    from core.models import CheckList
    cl = CheckList.objects.all()
    ## cl[0].checklistitem_set # created by django by reverse traverse

<!-- creates swagger documentation api  -->
    1. Creates base dir.: templates/doc.html
    https://www.django-rest-framework.org/topics/documenting-your-api/

    2. make changes to checklist/urls.py


<!-- giving permission to data which user only creates. -->
create file => core/permissions.py
