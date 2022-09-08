
from positions.models import Position
from django import forms


class AddPositionsForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = (
            'title',
            'description',
            'amount'
        )