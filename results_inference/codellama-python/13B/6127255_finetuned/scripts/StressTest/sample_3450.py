#join_time_premise = 2
#join_time_hypothesis = 8

# the hypothesis refers to the time when Jose joined, which is also mentioned in the premise
if join_time_hypothesis < join_time_premise:
    # check if the hypothesis value contradicts the time when Jose joined in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
# 