# Premise: Sam purchased 20 dozens of toys at the rate of Rs.
# Hypothesis: Sam purchased less than 20 dozens of toys at the rate of Rs.
# Golden Label: contradiction

toys_purchased_premise = 20
toys_purchased_hypothesis = 20

# the hypothesis refers to the number of toys purchased mentioned in the premise
if toys_purchased_hypothesis >= toys_purchased_premise:
    # check if the hypothesis value contradicts the premise, which states that more than 'toys_purchased_premise' were bought
    label = "contradiction"
else:
    # the premise gives the exact number of toys bought
    # any number of toys less than 'toys_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

