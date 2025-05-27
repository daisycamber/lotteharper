from django import forms
from .models import Survey, Answer
from feed.middleware import get_current_user

class UpdateSurveyForm(forms.ModelForm):
    question = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    def __init__(self, surv, *args, **kwargs):
        super(UpdateSurveyForm, self).__init__(*args, *kwargs)
        from feed.middleware import get_current_request
        r = get_current_request()
        from translate.translate import translate
        self.fields['priority'].initial = surv.priority
        self.fields['question'].initial = surv.question
        self.fields['answers_seperated'].initial = surv.answers_seperated
        self.fields['priority'].label = translate(r, 'Indexing priority', src='en')
        self.fields['question'].label = translate(r, 'A question to ask the visitor', src='en')
        self.fields['answers_seperated'].label = translate(r, 'Answers for the question, one per line', src='en')

    class Meta:
        model = Survey
        fields = ('priority', 'question', 'answers_seperated',)

class SurveyForm(forms.ModelForm):
    answer = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'survey-large-text'}),
    )
    def __init__(self, survey, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, *kwargs)
        from feed.middleware import get_current_request
        r = get_current_request()
        from translate.translate import translate
        from django.conf import settings
        self.fields['answer'].label = translate(r, survey.question, src=settings.DEFAULT_LANG)
        choices = []
        self.instance.user = r.user
        self.instance.survey = survey
        for c in survey.answers_seperated.split('\n'):
            choices+=[[translate(r, c, src=settings.DEFAULT_LANG), translate(r, c, src=settings.DEFAULT_LANG)]]
        self.fields['answer'].choices = choices

    class Meta:
        model = Answer
        fields = ('answer',)
