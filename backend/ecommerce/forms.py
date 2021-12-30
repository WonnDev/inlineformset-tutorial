from django import forms
from django.forms import inlineformset_factory

from .models import Order, OrderItems


class OrderForm(forms.ModelForm):
    required_css_class = 'required'

    nf = forms.IntegerField(label="Nota Fiscal")

    class Meta:
        model = Order
        fields = ('nf',)


class OrderItemsForm(forms.ModelForm):
    required_css_class = 'required'

    id = forms.IntegerField()

    class Meta:
        model = OrderItems
        fields = ('order', 'id', 'product', 'quantity', 'price')

    def __init__(self, *args, **kwargs):
        super(OrderItemsForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['order'].label = ''
        self.fields['order'].widget = forms.HiddenInput()

        self.fields['id'].label = ''
        self.fields['id'].widget = forms.HiddenInput()

        self.fields['price'].widget.attrs['step'] = 0.01


OrderItemsFormset = inlineformset_factory(
    Order,
    OrderItems,
    form=OrderItemsForm,
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
