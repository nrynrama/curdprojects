from django import forms
class ProductForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Your Product Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Number'
            }
        )
    )
    product_name = forms.CharField(
       label='Enter Your Product Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter Your Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    product_color = forms.CharField(
        label='Enter Your Product Color',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    product_class = forms.CharField(
        label='Enter Your Product Class',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    number_of_products = forms.IntegerField(
        label='Enter Number of Products',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Number of products'
            }
        )
    )
    customer_name = forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )
    mobile_number = forms.IntegerField(
        label='Enter Customer Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Customer Email ID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email ID'
            }
        )
    )


class UpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Product Id ',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID to Update'
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'New Product Cost'
            }
        )
    )

class DeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID to Delete'
            }
        )
    )




























































