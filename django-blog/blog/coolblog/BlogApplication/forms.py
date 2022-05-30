from .models import Digest, Review
from django.forms import ModelForm, TextInput, Textarea


class DigestForm(ModelForm):
    class Meta:
        model = Digest
        fields = ["title", "digest_text"]
        widgets = {
            "title": TextInput(attrs={"placeholder": "Введи заголовок дайджеста"}),
            "digest_text": Textarea(attrs={"placeholder": "Введи текст дайджеста"})
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["title", "review_text"]
        widgets = {
            "title": TextInput(),
            "review_text": Textarea()
        }
