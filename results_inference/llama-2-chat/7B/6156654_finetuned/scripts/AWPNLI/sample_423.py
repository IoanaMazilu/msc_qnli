shorts_price = 13.99
shirt_price = 12.14
returned_jacket_money = 7.43
total_spent = shorts_price + shirt_price
net_amount = total_spent - returned_jacket_money

# the hypothesis refers to the total amount of money Sandy spent on clothes
if net_amount == 17.5:
    # check if the hypothesis value and the calculated net amount are equal
    label = "entailment"
else:
    # if the hypothesis value and the calculated net amount are not equal, it's a contradiction
    label = "contradiction"

print(label)
