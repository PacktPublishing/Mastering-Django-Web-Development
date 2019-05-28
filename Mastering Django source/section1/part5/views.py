from django.shortcuts import render
from django.http import JsonResponse

class ProcessPayment(View):
    total = 620.00
    tax_rate = 0.06
    reward_discount = 0.05

    def get_amount(self):
        """ Get amount and return it somehow. """
        return JsonResponse({'amount': self.total})

    def get_tax(self):
        return JsonResponse({
            'tax_rate': self.tax_rate,
            'tax_amount': self.total * self.tax_rate,
            })

    def get_discount(self):
        return JsonResponse({
            'discount_rate': self.reward_discount,
            'savings': self.total * self.reward_discount,
            })

    def unknown(self):
        messages.error(self.request, 'Unknown operator account!')
        return redirect('payment_error')

    def get(self, request, *args, **kwargs):
        handler = getattr(self, 'get_%s' % kwargs['operator'], self.unknown)
        return handler()
