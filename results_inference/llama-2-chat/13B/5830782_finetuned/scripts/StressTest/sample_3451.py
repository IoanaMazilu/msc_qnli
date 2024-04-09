months_premise = 8
months_hypothesis = 2

# the hypothesis talks about the number of months Jose joined later, referenced also in the premise
if months_hypothesis >= months_premise:
    # check if the hypothesis value contradicts the estimate of less than'months_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of months
    # any number of months less than'months_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
