trumpet_price_premise = 145.16
songbook_price_premise = 5.84
net_amount_hypothesis = 134.7

# the hypothesis refers to the net amount spent by Mike, which is also mentioned in the premise
# compute the net amount spent by Mike from the premise
net_amount_premise = trumpet_price_premise - songbook_price_premise
if net_amount_hypothesis!= net_amount_premise:
    # check if the net amount from the hypothesis contradicts the net amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
