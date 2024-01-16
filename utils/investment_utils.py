class InvestmentUtils:

    def calculate_compound_interest(
            self, initial_value, interest_rate, period, periodic_application=0) -> float:
        
        final_amount = (initial_value * ((1 + interest_rate)**period)  
                        + periodic_application * (
                                ((1 + interest_rate)**period - 1) / interest_rate
                            )
                        )
        
        return round(final_amount,2)