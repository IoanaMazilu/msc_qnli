dawson_premise = 28
dawson_hypothesis = 38

# the hypothesis refers to the time taken by Dawson to run the first leg of the course
if dawson_hypothesis <= dawson_premise:
    # check if the hypothesis value contradicts the estimate of more than 'dawson_premise'
    label = "contradiction"
elif dawson_hypothesis > dawson_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the time taken by Dawson
    # any time taken greater than 'dawson_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
