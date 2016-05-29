from django import forms

class CheckoutForm(forms.Form):

    postal_error_messages = {
        'invalid': 'Format must be A1A 1A1'
    }

    BRITISH_COLUMBIA = 'BC'
    ALBERTA = 'AB'
    SASKATCHEWAN = 'SK'
    MANITOBA = 'MB'
    ONTARIO = 'ON'
    QUEBEC = 'QC'
    NUNAVUT = 'NU'
    NORTHWEST_TERRITORIES = 'NT'
    YUKON = 'YT'
    NEWFOUNDLAND_LABRADOR = 'NL'
    NEW_BRUNSWICK = 'NB'
    NOVA_SCOTIA = 'NS'
    PRINCE_EDWARD_ISLAND = 'PE'

    PROVINCE_CHOICES = (
        (None, '--- Choose A Province ---'),
        (ALBERTA, 'Alberta'),
        (BRITISH_COLUMBIA, 'British Columbia'),
        (MANITOBA, 'Manitoba'),
        (NEW_BRUNSWICK, 'New Brunswick'),
        (NEWFOUNDLAND_LABRADOR, 'Newfoundland/Labrador'),
        (NORTHWEST_TERRITORIES, 'Northwest Territories'),
        (NOVA_SCOTIA, 'Nova Scotia'),
        (NUNAVUT, 'Nunavut'),
        (ONTARIO, 'Ontario'),
        (PRINCE_EDWARD_ISLAND, 'Prince Edward Island'),
        (QUEBEC, 'Quebec'),
        (SASKATCHEWAN, 'Saskatchewan'),
        (YUKON, 'Yukon'),
    )

    first_name = forms.CharField()
    last_name = forms.CharField()
    address_1 = forms.CharField()
    address_2 = forms.CharField(required=False)
    city = forms.CharField()
    province = forms.ChoiceField(choices=PROVINCE_CHOICES, required=True)
    postal_code = forms.RegexField(regex=r'[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d', error_messages=postal_error_messages)
    phone_number = forms.CharField(required=False)
    email = forms.EmailField()

