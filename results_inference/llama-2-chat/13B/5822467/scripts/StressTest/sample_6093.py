unit_digits_premise = 9
unit_digits_hypothesis = 8

# the hypothesis refers to the product of all possible unit digits of Sophie Germain primes greater than 8
if unit_digits_hypothesis <= unit_digits_premise:
    # check if the hypothesis value contradicts the estimate of the product of all possible unit digits in the premise
    label = "contradiction"
elif unit_digits_premise!= unit_digits_hypothesis:
    # check if the hypothesis value contradicts the product of all possible unit digits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
