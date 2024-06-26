yolanda_rate_premise = 3
bob_rate_premise = 4
yolanda_rate_hypothesis = 5
bob_rate_hypothesis = 4

# the hypothesis refers to Yolanda's and Bob's walking rates mentioned in the premise
if yolanda_rate_premise >= yolanda_rate_hypothesis:
    # check if the rate of 'yolanda_rate_hypothesis' contradicts the rate of Yolanda in the premise
    label = "contradiction"
elif bob_rate_hypothesis != bob_rate_premise:
    # check if the rate of Bob in the hypothesis contradicts the rate of Bob reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and rates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
