net_amount_premise = 13.99 + 12.14 - 7.43
hypothesis_amount = 17.5

# check if the net amount spent on clothes in the hypothesis contradicts the premise
if hypothesis_amount!= net_amount_premise:
    label = "contradiction"
elif hypothesis_amount > net_amount_premise:
    # check if the net amount spent on clothes in the hypothesis entails the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
