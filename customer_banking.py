# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Formatted output print function
def print_output(account_type, balance, interest):
    printed_dashes = "-" * 50
    print(printed_dashes)
    print("Your", account_type, "account balance is $", format(balance, ',.2f'))
    print("Your", account_type, "interest earned is $", format(interest, ',.2f'))
    print(printed_dashes)

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    while True:
        savings_balance = input("Please enter savings balance as number with decimals, no currency or commas: ")
        try:
            savings_balance = float(savings_balance)
            break
        except ValueError:
            return False

    while True:
        savings_interest = input("Please enter savings interest rate as number with decimals, no percentage or commas: ")
        try:
            savings_interest = float(savings_interest)
            break
        except ValueError:
            return False

    while True:
        savings_maturity = input("Please enter number of months with no decimals: ")
        if savings_maturity.isdigit():
            savings_maturity = int(savings_maturity)
            break

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print_output("Savings", updated_savings_balance, interest_earned)
        
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    # This code below can be a function also, as it gets executed the same for both types of accounts - CD and Savings
    while True:
        cd_balance = input("Please enter CD balance as number with decimals, no currency or commas: ")
        try:
            cd_balance = float(cd_balance)
            break
        except ValueError:
            return False

    while True:
        cd_interest = input("Please enter CD interest rate as number with decimals, no percentage or commas: ")
        try:
            cd_interest = float(cd_interest)
            break
        except ValueError:
            return False

    while True:
        cd_maturity = input("Please enter number of months with no decimals: ")
        if cd_maturity.isdigit():
            cd_maturity = int(cd_maturity)
            break

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print_output("CD", updated_cd_balance, interest_earned)

if __name__ == "__main__":
    # Call the main function.
    main()
