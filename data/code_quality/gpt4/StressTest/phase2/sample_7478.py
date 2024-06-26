units_digit_product_premise = 8
units_digit_product_hypothesis = 4

# the hypothesis refers to the product of units digits of Sophie Germain primes greater than a certain value
if units_digit_product_hypothesis < units_digit_product_premise:
    # check if the 'units_digit_product_hypothesis' contradicts the value in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
