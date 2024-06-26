shorts_price = 13.99
shirt_price = 12.14
jacket_return_price = 7.43

# Calculate the total amount spent on clothes
total_spent = shorts_price + shirt_price - jacket_return_price

# The hypothesis refers to the total amount spent on clothes
if total_spent!= 17.5:
    # Check if the total amount spent on clothes contradicts the hypothesis
    label = "contradiction"
else:
    # If the total amount spent on clothes does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
