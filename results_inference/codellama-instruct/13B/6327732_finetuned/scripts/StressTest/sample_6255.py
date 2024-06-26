discount_premise = 20
discount_hypothesis = 30

# the hypothesis talks about the discount percentage and the amount paid by each person
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an estimate for the discount percentage and the amount paid by each person
    # any discount percentage less than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
