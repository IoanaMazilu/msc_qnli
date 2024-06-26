bonds_purchased_premise = 4000
bonds_purchased_hypothesis = 5000

# the hypothesis refers to the amount of bonds purchased, also mentioned in the premise
if bonds_purchased_hypothesis == bonds_purchased_premise:
    # check if the exact amount of bonds purchased in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # any amount of bonds greater than 'bonds_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
