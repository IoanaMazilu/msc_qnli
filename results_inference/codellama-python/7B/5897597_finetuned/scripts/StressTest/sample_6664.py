chiefs_premise = 6
chiefs_hypothesis = 7

# the hypothesis talks about the number of Joint Chiefs of Staff at a meeting, referenced also in the premise
if chiefs_hypothesis <= chiefs_premise:
    # check if the hypothesis value contradicts the estimate of more than 'chiefs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of chiefs
    # any number of chiefs greater than 'chiefs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
