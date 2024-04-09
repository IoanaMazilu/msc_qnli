apples_premise = 7
apples_hypothesis = 4

# the hypothesis talks about the number of apples Maddie has, referenced also in the premise
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apples_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of apples, and the hypothesis value is consistent with that estimate
    label = "entailment"

print(label)
