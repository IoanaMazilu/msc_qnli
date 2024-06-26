average_raise_premise = 7
average_raise_hypothesis = 2

# the hypothesis talks about the points Jerry wants to raise his average by, referenced also in the premise
if average_raise_hypothesis >= average_raise_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_raise_premise'
    label = "contradiction"
elif average_raise_hypothesis < average_raise_premise:
    # the premise gives only an estimate for the points Jerry wants to raise his average by
    # any number of points less than 'average_raise_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
