from mongoengine import (Document, StringField, IntField, 
                         FloatField, queryset_manager)

class InvestmentSimulation(Document):

    COMPENSATION_CHOICES = ['post-fixed', 'pre-fixed']


    name = StringField(required=True, min_length=1)
    months_invested = IntField(required=True, min_value=1)
    initial_value = FloatField(required=True, min_value=0)
    monthly_investment = FloatField(required=True, min_value=0)
    monthly_interest_rate = FloatField(required=True, min_value=0)
    compensation = StringField(required=True)
    final_amount = FloatField(required=True, min_value=0)

    @queryset_manager
    def objects(cls, queryset):
        return queryset
    
    @classmethod
    def get_average_final_amount(cls):
        
        average_final_amount = cls.objects.average('final_amount')
        
        return average_final_amount
    
    @classmethod
    def get_document_with_max_final_amount(cls):

        with_max_amount = cls.objects.order_by('-final_amount').first()

        return with_max_amount
    
    @classmethod
    def get_document_with_min_final_amount(cls):

        with_min_amount = cls.objects.order_by('final_amount').first()

        return with_min_amount
    
    @classmethod
    def get_document_with_max_monthly_investment(cls):

        with_monthly_investment = cls.objects.order_by('-monthly_investment').first()

        return with_monthly_investment
    
    @classmethod
    def get_document_with_min_monthly_investment(cls):

        with_monthly_investment = cls.objects.order_by('monthly_investment').first()

        return with_monthly_investment