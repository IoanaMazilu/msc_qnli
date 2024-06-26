age_premise = 6
age_hypothesis = 3

# the hypothesis talks about Arun's age in the future, referenced also in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of Arun's age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for Arun's age in the future, which cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
