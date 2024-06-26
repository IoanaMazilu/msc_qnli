apples_premise = 360
apples_hypothesis = 460

# the hypothesis refers to the number of apples Anita has, which is also mentioned in the premise
if apples_premise >= apples_hypothesis:
    # check if the number of apples in the premise contradicts the estimate of less than 'apples_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
