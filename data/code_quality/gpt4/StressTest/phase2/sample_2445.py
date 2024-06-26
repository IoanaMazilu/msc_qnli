product_age_premise = 32
product_age_hypothesis = 72

# the hypothesis refers to the same product of ages as the premise
if product_age_hypothesis <= product_age_premise:
    # check if the hypothesis value contradicts the exact value of 'product_age_premise'
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise, but it also cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
