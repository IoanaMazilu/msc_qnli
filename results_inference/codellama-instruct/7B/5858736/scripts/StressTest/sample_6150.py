# define variables for the numerical entities in the premise and hypothesis
premise_total_hours = 41
premise_paid_amount = 1
hypothesis_total_hours = 71
hypothesis_paid_amount = 1

# calculate the number of hours worked by Harry
harry_total_hours = premise_total_hours - hypothesis_total_hours

# check if the hypothesis values contradict the premise ones
if harry_total_hours < 0:
    # the hypothesis value contradicts the premise one, so the hypothesis is a contradiction
    label = "contradiction"
elif harry_total_hours == 0:
    # the hypothesis value is consistent with the premise one, so the hypothesis is neutral
    label = "neutral"
else:
    # the hypothesis value is greater than the premise one, so the hypothesis is entailed
    label = "entailment"

print(label)
