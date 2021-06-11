# has_height_income = False
has_good_credit = True
has_criminal_records = True

# AND: both condition must be true
# if has_good_credit and has_height_income:
#   print("AND: Eligible for loan")

# # OR: At least one condition must be true
# if has_good_credit or has_height_income:
#   print("OR: Eligible for loan")

# NOT:
if has_good_credit and not has_criminal_records:
  print("NOT: Eligible for loan")