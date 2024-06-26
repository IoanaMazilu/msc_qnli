chiefs_premise = 7
chiefs_hypothesis = 6

# the hypothesis talks about the number of Joint Chiefs of Staff, referenced also in the premise
if chiefs_hypothesis <= chiefs_premise:
    # check if the hypothesis value contradicts the estimate of 'chiefs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Joint Chiefs of Staff
    # any number of Joint Chiefs of Staff greater than 'chiefs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
