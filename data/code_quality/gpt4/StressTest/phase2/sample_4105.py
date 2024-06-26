months_premise = 7
months_hypothesis = 8

# the hypothesis talks about the number of months Alex joined him later, referenced also in the premise
if months_hypothesis <= months_premise:
    # check if the hypothesis value contradicts the estimate of more than 'months_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of months
    # any number of months greater than 'months_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
