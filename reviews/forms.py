from django import forms
from .models import Review
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

class ReviewForm(forms.ModelForm):
    image = ProcessedImageField(
        spec_id='reviews:image',
        processors=[ResizeToFill(100,100)],
        format='JPEG',
        options={'quality' : 90},
        required=False,
    )
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['movie'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'