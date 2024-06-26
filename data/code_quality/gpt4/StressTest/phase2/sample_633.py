regular_hours_premise = 40
regular_hours_hypothesis = 80
regular_rate = 7

# the hypothesis refers to the number of regular hours Michael works per week, mentioned also in the premise
if regular_hours_hypothesis <= regular_hours_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only a specific number of regular hours 
    # any number of regular hours less than 'regular_hours_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
