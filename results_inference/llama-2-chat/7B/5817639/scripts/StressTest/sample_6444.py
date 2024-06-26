years_premise = 14
years_hypothesis = 84

# the hypothesis talks about the difference in age between two people, referenced also in the premise
if years_hypothesis <= years_premise:
    # check if the hypothesis value contradicts the estimate of 'years_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the difference in age, which the hypothesis cannot explicitly entail
    label = "neutral"

print(label)
