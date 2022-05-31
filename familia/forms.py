from django import forms


class PersonaForm(forms.Form):
    nombre= forms.CharField(label="Nombre")
    altura= forms.FloatField(widget=forms.NumberInput(attrs={"placeholder" : "1,75 m"}))
    fecha_nacimiento= forms.DateField(label = "fecha_nacimiento", input_formats=["%d/%m/%Y"],
    widget=forms.TextInput(attrs = {"placeholder" : "Fecha de nacimiento:"}))
    email = forms.EmailField(label="Email")

class BuscarPersonaForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")
    