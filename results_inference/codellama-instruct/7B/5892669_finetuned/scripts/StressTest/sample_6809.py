yolandas_rate_premise = 3
bob_rate_premise = 4
yolandas_rate_hypothesis = 5
bob_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Yolanda and Bob mentioned in the premise
if yolandas_rate_premise!= yolandas_rate_hypothesis:
    # check if the walking rate of Yolanda in the hypothesis contradicts the walking rate of Yolanda in the premise
    label = "contradiction"
elif bob_rate_premise!= bob_rate_hypothesis:
    # check if the walking rate of Bob in the hypothesis contradicts the walking rate of Bob in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
