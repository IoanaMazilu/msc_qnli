discount_premise = 30
discount_hypothesis = 20
discount_value_premise = 4
discount_value_hypothesis = 4

# The hypothesis talks about the discount percentage and the discount value, both are also referenced in the premise
if discount_hypothesis >= discount_premise:
    # Check if the discount percentage in the hypothesis contradicts the 'less than discount_premise' percentage in the premise
    label = "contradiction"
elif discount_value_hypothesis != discount_value_premise:
    # Check if the discount value in the hypothesis contradicts the discount value in the premise
    label = "contradiction"
else:
    # The premise gives only a maximum for the discount percentage
    # Any discount percentage less than 'discount_premise' and equal discount value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
