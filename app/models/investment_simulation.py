from mongoengine import (Document, StringField, IntField, 
                         FloatField, ValidationError)

class InvestmentSimulation(Document):

    COMPENSATION_CHOICES = ['post-fixed', 'pre-fixed']


    name = StringField(required=True, min_length=1)
    months_invested = IntField(required=True, min_value=1)
    initial_value = FloatField(required=True, min_value=0)
    monthly_investment = FloatField(required=True, min_value=0)
    monthly_interest_rate = FloatField(required=True, min_value=0)
    compensation = StringField(required=True)

    def clean(self):
        if self.compensation not in self.COMPENSATION_CHOICES:
            raise ValidationError(f'Compensation must be one of these: {", ".join(self.COMPENSATION_CHOICES)}')
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)