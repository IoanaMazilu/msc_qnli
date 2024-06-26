kg_kiwi_premise = 8
kg_kiwi_hypothesis = 5
avg_rate_premise = 360

# the hypothesis refers to the amount of kiwi fruit bought and the average rate
if kg_kiwi_hypothesis <= kg_kiwi_premise:
    # check if the estimate of 'kg_kiwi_hypothesis' contradicts the amount of kiwi fruit bought in the premise
    label = "contradiction"
elif avg_rate_premise!= avg_rate_hypothesis:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
