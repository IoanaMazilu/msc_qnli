units_digit_product_premise = 8
units_digit_product_hypothesis = 7

# the hypothesis refers to a product of the units digits of Sophie Germain primes, as does the premise
if units_digit_product_hypothesis >= units_digit_product_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif units_digit_product_hypothesis < units_digit_product_premise:
    # check if the premise value entails the hypothesis
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
