deal_value_premise = 300000000
deal_value_hypothesis = 300000000

# the hypothesis mentions the value of the deal, which is also mentioned in the premise
if deal_value_hypothesis!= deal_value_premise:
    # check if the deal value in the hypothesis contradicts the deal value reported in the premise
    label = "contradiction"
else:
    # if the deal value in the hypothesis does not contradict the deal value in the premise, we can infer entailment
    label = "entailment"

print(label)
