age_premise = 5/3
age_hypothesis = 7/3

# the hypothesis refers to the age of the person in the future, relative to Tom's age
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of 'age_premise'
    label = "contradiction"
elif age_hypothesis > age_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the future age
    # any age less than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
