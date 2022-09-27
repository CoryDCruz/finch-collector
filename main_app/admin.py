from django.contrib import admin
from .models import Finch
from .models import Toy
from .models import Feeding
from .models import Photo

# Register your models here.
admin.site.register(Finch)
admin.site.register(Toy)
admin.site.register(Feeding)
admin.site.register(Photo)
