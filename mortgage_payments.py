'''
    CS5001
    Spring 2023
    HW3

    Brendan Sheehan

    This program returns the principal owed at the end of a specified month
'''
    
def principal_remaining_by(principal, annual_interest_rate,
                           duration_in_months, by_month):

    '''
    Function: principal_remaining_by

    Parameters:
    original principal
    annual interest rate
    duration in months of mortgage
    the chosen month of the mortgage

    Return: principal owed at the end of a specific month

    Pre Conditions: Assume inputs are validated prior to calling function.
    eg. all parameters are positive numbers, month parameters = int and
    by month <= duration_in_months

    '''

    # formula for monthly interest rate gives .005
    monthly_interest_rate = (annual_interest_rate / 12) * 0.01

    # formula that calculates mortgage payment
    top_equation = monthly_interest_rate * ((1 + monthly_interest_rate)
                                            ** duration_in_months)
    bottom_equation = (1 + monthly_interest_rate)
    ** duration_in_months - 1
    mortgage_payment = principal * (top_equation / bottom_equation)
    
    # formula that calculates the amount of interest due 
    interest_due = monthly_interest_rate * principal

    # formula that calculates the amount of principal due in a month
    principal_due = mortgage_payment - interest_due

    month_counter = duration_in_months - by_month  

    # loop to calculate principal for a given month
    while duration_in_months > month_counter:

        interest_due = monthly_interest_rate * principal

        principal_due = mortgage_payment - interest_due
        
        duration_in_months = duration_in_months - 1

        principal = principal - principal_due

    return (round(principal, 2))
