chiefs_premise = 5
chiefs_hypothesis = 1

# the hypothesis talks about a meeting of a different number of Joint Chiefs than the premise
if chiefs_hypothesis <= chiefs_premise:
    # check if the hypothesis value contradicts the estimate of 'chiefs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Joint Chiefs
    # any number of Joint Chiefs greater than 'chiefs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
