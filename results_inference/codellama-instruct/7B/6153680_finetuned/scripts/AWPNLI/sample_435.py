# The hypothesis refers to the amount of money left in Abe's family's account
# The premise gives the amount of money in the account and the amount spent

# Calculate the amount of money left in the account
left_money = 6359.0 - 3485.0

# Check if the hypothesis value matches the calculated value
if left_money == 2870.0:
    label = "entailment"
else:
    label = "contradiction"

print(label)
