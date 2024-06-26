yolanda_rate_premise = 3
yolanda_rate_hypothesis = 5
bob_rate_premise = 4
bob_rate_hypothesis = 4

# the hypothesis talks about Yolanda and Bob's walking rates, referenced also in the premise
if yolanda_rate_hypothesis!= yolanda_rate_premise:
    # check if Yolanda's walking rate in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif bob_rate_hypothesis!= bob_rate_premise:
    # check if Bob's walking rate in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
