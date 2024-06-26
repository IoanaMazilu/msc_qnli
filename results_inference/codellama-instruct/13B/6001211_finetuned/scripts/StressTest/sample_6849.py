apples_billy_premise = 10
apples_billy_hypothesis = 20

# the hypothesis refers to the number of apples Billy has, which is also mentioned in the premise
if apples_billy_premise >= apples_billy_hypothesis:
    # check if the number of apples in the premise contradicts the estimate of less than 'apples_billy_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
