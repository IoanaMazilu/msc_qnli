yolanda_rate_premise = 3
bob_rate_premise = 4
yolanda_rate_hypothesis = 5
bob_rate_hypothesis = 4

# the hypothesis and premise provide the walking rates for Yolanda and Bob
if yolanda_rate_hypothesis != yolanda_rate_premise:
    # check if the walking rate for Yolanda stated in the hypothesis contradicts the one mentioned in the premise
    label = "contradiction"
elif bob_rate_hypothesis != bob_rate_premise:
    # check if the walking rate for Bob stated in the hypothesis contradicts the one stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
