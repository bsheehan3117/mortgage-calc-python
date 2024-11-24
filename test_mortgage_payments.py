'''
    CS5001
    Spring 2023
    HW3

    Brendan Sheehan

    This program tests the mortgage_payments function
'''

from mortgage_payments import principal_remaining_by

def test_principal_remaining_by(principal, annual_interest_rate,
                                duration_in_months, by_month, expected):

    '''
    Function: principal_remaining_by
    Parameters:
    original principal
    annual interest rate
    duration in months of mortgage
    the chosen month of the mortgage

    Return: principal owed at the end of a specific month
    '''
    print("Finding the remaining mortgage principal by month", by_month)

    actual = principal_remaining_by(principal, annual_interest_rate,
                                    duration_in_months, by_month)
    print("'\tExpected = ", expected)
    print("\tResult = ", actual)

def main():

    # test 1
    test_principal_remaining_by(600000, 6, 360, 2, 598802.41)

    # test 2
    test_principal_remaining_by(600000, 6, 120, 34, 464678.83)

    # test 3
    test_principal_remaining_by(600000, 6, 360, 45, 569941.22)

    # test 4
    test_principal_remaining_by(600000, 6, 120, 34, 464678.83)

    # test 5
    test_principal_remaining_by(135000, 6, 240, 12, 131395.77)

    # test 6
    test_principal_remaining_by(600000, 3, 360, 10, 589587.15)


if __name__ == "__main__":
    main()
    
