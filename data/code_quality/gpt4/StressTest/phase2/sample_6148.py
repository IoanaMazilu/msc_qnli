hours_regular_premise = 70
hours_regular_hypothesis = 40

# the hypothesis refers to the hours of regular work mentioned in the premise
if hours_regular_hypothesis > hours_regular_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours reported in the premise
    label = "contradiction"
else:
    # if the number of regular hours in the hypothesis is less than or equal to the number of regular hours in the premise, it does not contradict the premise, but cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
