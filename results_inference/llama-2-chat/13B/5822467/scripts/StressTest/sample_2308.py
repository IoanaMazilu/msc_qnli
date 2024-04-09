doubled_speed_premise = 2
hours_premise = 5

# define variables for the numerical entities in the premise
anne_speed_premise = doubled_speed_premise
hours_hypothesis = 3

# check if the hypothesis value contradicts the premise estimate
if hours_hypothesis < hours_premise:
    label = "contradiction"
elif hours_hypothesis == hours_premise:
    # the hypothesis value is consistent with the premise estimate
    label = "neutral"
else:
    # the premise estimate is less than the hypothesis value
    label = "entailment"

print(label)
