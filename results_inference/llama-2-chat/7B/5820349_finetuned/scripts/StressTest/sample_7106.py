regular_hours_premise = 30
regular_hours_hypothesis = 30

# the hypothesis refers to the number of regular hours Harry works in a week
if regular_hours_hypothesis >= regular_hours_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif regular_hours_hypothesis < regular_hours_premise:
    # if the hypothesis value is less than the premise, it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
