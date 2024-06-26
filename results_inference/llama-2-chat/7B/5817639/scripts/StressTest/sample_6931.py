age_premise = 2
age_hypothesis = 6

# the hypothesis talks about Sandy's age in the future, referenced also in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_premise' years
    label = "contradiction"
else:
    # the premise gives only an estimate for Sandy's age in the future
    # any age greater than 'age_premise' years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
