returns_premise = 2
returns_hypothesis = 4

# the hypothesis talks about the returns of the original investment, referenced also in the premise
if returns_hypothesis <= returns_premise:
    # check if the hypothesis value contradicts the estimate of more than 'returns_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the returns
    # any returns greater than 'returns_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
