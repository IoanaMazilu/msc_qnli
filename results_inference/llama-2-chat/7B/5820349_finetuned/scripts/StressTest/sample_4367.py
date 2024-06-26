regular_hours_premise = 40
regular_hours_hypothesis = 40

# the hypothesis refers to the number of regular hours worked by James, mentioned in the premise
if regular_hours_hypothesis <= regular_hours_premise:
    # check if the hypothesis value contradicts the number of regular hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of regular hours
    # any number of regular hours greater than'regular_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
