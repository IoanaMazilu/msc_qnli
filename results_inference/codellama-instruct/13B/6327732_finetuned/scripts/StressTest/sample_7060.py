time_cara_premise = 20
time_cara_hypothesis = 90

# the hypothesis refers to the time difference between Cara and Dan
if time_cara_hypothesis <= time_cara_premise:
    # check if the estimate of 'time_cara_hypothesis' contradicts the time difference in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than 'time_cara_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
