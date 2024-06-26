yolanda_rate_premise = 3
bob_rate_premise = 4
yolanda_rate_hypothesis = 5
bob_rate_hypothesis = 4

# the hypothesis talks about the walking rates of Yolanda and Bob, referenced also in the premise
if yolanda_rate_hypothesis!= yolanda_rate_premise:
    # check if the walking rate of Yolanda in the hypothesis contradicts the walking rate of Yolanda reported in the premise
    label = "contradiction"
elif bob_rate_hypothesis!= bob_rate_premise:
    # check if the walking rate of Bob in the hypothesis contradicts the walking rate of Bob reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
