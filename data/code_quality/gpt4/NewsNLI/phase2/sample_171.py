deal_value_premise = 3000000000
deal_value_hypothesis = 3000000000

# the hypothesis mentions the deal value between Lakers and Time Warner, which is also mentioned in the premise
if deal_value_hypothesis != deal_value_premise:
    # check if the deal value in the hypothesis contradicts the deal value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
