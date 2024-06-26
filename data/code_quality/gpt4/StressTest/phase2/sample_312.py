leo_gain_premise = 10
leo_gain_hypothesis = 30
weight_percentage_premise = 50
weight_percentage_hypothesis = 50

# the hypothesis talks about the weight gain of Leo and its relationship with his sister's weight, also referenced in the premise
if leo_gain_hypothesis < leo_gain_premise and weight_percentage_hypothesis == weight_percentage_premise:
    # check if the hypothesis value contradicts the estimate of 'leo_gain_premise' for the same weight percentage
    label = "contradiction"
elif leo_gain_hypothesis >= leo_gain_premise and weight_percentage_hypothesis == weight_percentage_premise:
    # check if the hypothesis value is consistent with the premise and if the weight percentage is the same
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones and cannot be explicitly entailed, we infer neutrality
    label = "neutral"

print(label)
