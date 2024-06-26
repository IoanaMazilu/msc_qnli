ana_premise = 2
ana_hypothesis = 8

# the hypothesis talks about Ana's position before P, referenced also in the premise
if ana_hypothesis <= ana_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ana_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Ana's position
    # any position greater than 'ana_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
