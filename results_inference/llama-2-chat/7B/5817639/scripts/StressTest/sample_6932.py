years_premise = 6
years_hypothesis = 3

# the hypothesis talks about Sandy's age in the future, referenced also in the premise
if years_hypothesis <= years_premise:
    # check if the hypothesis value contradicts the estimate of 'years_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for Sandy's age in the future, but does not provide enough information to entail the hypothesis
    label = "neutral"

print(label)
