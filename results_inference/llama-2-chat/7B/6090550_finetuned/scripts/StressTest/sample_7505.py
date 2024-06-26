essential_info: 10
hypothesis_time: 60

# the hypothesis talks about the time when Pat stops to stretch, referenced also in the premise
if hypothesis_time == premise_time:
    # check if the hypothesis time is equal to the premise time
    label = "entailment"
else:
    # the hypothesis time is not equal to the premise time, so we check if it contradicts the premise
    label = "contradiction"

print(label)
