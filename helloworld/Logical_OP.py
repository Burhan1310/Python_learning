# if applicant has high income AND good credit
# Eligible for Loan
# has_high_income = False
# has_good_credit =True
#
# if has_high_income and has_good_credit:
#     print("Eligible for Loans")
#
# else:
#     print("Not Eligible for loan ")


# if applicant has high income OR good credit
# Eligible for Loan
# has_high_income = True
# has_good_credit = False
#
# if has_high_income or has_good_credit:
#     print("You're Eligible for Loan")
# else:
#     print("Sorry, you're not Eligible for Loan")

# if applicant has good credit AND doesn't have criminal record
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("You're Eligible for Loan")
else:
    print("Sorry, you're not eligible for Loan")

