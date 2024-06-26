seconds_premise = 7
seconds_hypothesis = 6

# the hypothesis refers to the time Henry takes to run the second leg of the course mentioned in the premise
if seconds_hypothesis >= seconds_premise:
    # check if the hypothesis estimate contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than'seconds_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
