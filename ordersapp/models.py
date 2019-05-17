from django.db import models

from django.conf import settings
from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'pending'),
        (SENT_TO_PROCEED, 'processing'),
        (PAID, 'paid'),
        (PROCEEDED, 'proceed'),
        (READY, 'shipped'),
        (CANCEL, 'canceled'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated', auto_now=True)
    status = models.CharField(verbose_name='status', max_length=3, choices=ORDER_STATUS_CHOICES, default=FORMING)
    is_active = models.BooleanField(verbose_name='active', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_total_quantity(self):
        # items = self.orderitems.select_related()
        # return sum(list(map(lambda x: x.quantity, items)))
        items = self.orderitems.values_list('quantity', flat=True)
        return sum(items)

    def get_product_type_quantity(self):
        # items = self.orderitems.select_related()
        # return len(items)
        return self.orderitems.count()

    def get_total_cost(self):
        items = self.orderitems.select_related('product')
        # return sum(list(map(lambda x: x.quantity * x.product.price, items)))
        return sum([el.quantity * el.product.price for el in items])

    # переопределяем метод, удаляющий объект
    def delete(self):
        for item in self.orderitems.all():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()

    def __str__(self):
        return f'Current order: {self.id}'


# class OrderItemQuerySet(models.QuerySet):

#    def delete(self, *args, **kwargs):
#        for object in self:
#            object.product.quantity += object.quantity
#            object.product.save()
#        super().delete(*args, **kwargs)


class OrderItem(models.Model):
    #    objects = OrderItemQuerySet.as_manager()
    order = models.ForeignKey(Order, related_name="orderitems", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.filter(pk=pk).first()

# переопределяем метод, сохранения объекта
#    def save(self, *args, **kwargs):
#        if self.pk:
#            self.product.quantity -= self.quantity - OrderItem.get_item(self.pk).quantity
#        else:
#            self.product.quantity -= self.quantity
#        self.product.save()
#        super().save(*args, **kwargs)

#    def delete(self):
#        self.product.quantity += self.quantity
#        self.product.save()
#        super().delete()
