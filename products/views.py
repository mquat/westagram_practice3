from django.http  import JsonResponse
from django.views import View

from .models import Product

class ProductListView(View):
    def get(self,request):
        category_id = int(request.GET.get('category_id', None))
        offset      = int(request.GET.get('offset', 0))
        limit       = int(request.GET.get('limit', 10))

        products = Product.objects.filter(category_id = category_id)[offset : offset+limit]
        
        result = [{
            'id'        : product.id,
            'name'      : product.name,
            'price'     : product.price,
            'image_url' : [{image.image_url} for image in product.image_set.all()]
        } for product in products]

        return JsonResponse({'product_list' : result}, status = 200)

class ProductDetailView(View):
    def get(self,request,product_id):
        product = Product.objects.get(id = product_id)

        result = {
            'name'        : product.name,
            'origin'      : product.origin,
            'volume'      : product.volume,
            'description' : product.description,
            'summary'     : product.summary,
            'price'       : product.price,
            'image_url'   : [{image.image_url} for image in product.image_set.all()]
        }

        return JsonResponse({'product':result}, status=200)