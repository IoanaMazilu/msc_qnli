regular_hours_premise = 35
regular_hours_hypothesis = 35

# the hypothesis refers to the number of regular hours Harry works per week, mentioned in the premise
if regular_hours_hypothesis <= regular_hours_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific number of regular hours Harry works per week
    # any number of regular hours greater than'regular_hours_premise' contradicts the premise
    label = "contradiction"

print(label)
