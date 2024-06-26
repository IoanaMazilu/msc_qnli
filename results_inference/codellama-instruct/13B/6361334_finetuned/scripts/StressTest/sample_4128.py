time_cara_leaves_premise = 60
time_cara_leaves_hypothesis = 30

# the hypothesis refers to the time difference between Cara and Dan leaving City A
if time_cara_leaves_hypothesis <= time_cara_leaves_premise:
    # check if the estimate of 'time_cara_leaves_hypothesis' contradicts the time difference in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than 'time_cara_leaves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
