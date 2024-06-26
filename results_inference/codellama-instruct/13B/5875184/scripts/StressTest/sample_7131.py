days_walked_premise = 3
days_walked_hypothesis = 2

# the hypothesis refers to the number of days walked mentioned in the premise
if days_walked_premise <= days_walked_hypothesis:
    # check if the estimate of 'days_walked_hypothesis' contradicts the number of days walked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days walked
    # any number of days greater than 'days_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
