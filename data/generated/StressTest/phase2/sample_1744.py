# Premise: At the end of'n'years, Sandy got back more than 2 times the original investment.
# Hypothesis: At the end of'n'years, Sandy got back 4 times the original investment.
# Golden Label: neutral

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

