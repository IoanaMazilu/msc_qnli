ime_premise = 21
time_hypothesis = 11

# the hypothesis refers to the number of hours Harry works in a week, which is also mentioned in the premise
if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact number of hours Harry works
    # any number of hours greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
