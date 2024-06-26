costa_deal_premise = 5.1e9
costa_deal_hypothesis = 5.1e9

# the hypothesis mentions the deal amount for Costa, which is also mentioned in the premise
if costa_deal_hypothesis!= costa_deal_premise:
    # check if the deal amount in the hypothesis contradicts the deal amount in the premise
    label = "contradiction"
else:
    # if the deal amount in the hypothesis does not contradict the deal amount in the premise, we can infer entailment
    label = "entailment"

print(label)
