from django.shortcuts import render

# Create your views here.
class CartView(View):
    total = 620.00
    tax_rate = 0.06
    
    def get_total(self):
        return self.total

    def get_tax(self):
        return self.total * self.tax_rate

    def get(request, *args, **kwargs):
        context = {
            'subtotal': self.get_total(),
            'tax': self.get_tax(),
            'total': self.get_total() + self.get_tax(),
        }

        return render(request, 'cart.html', context)
