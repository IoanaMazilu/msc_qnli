total_money_premise = 5887
total_money_hypothesis = 4887

# the hypothesis talks about the total money divided between Shyam and Ram, which is also mentioned in the premise
if total_money_premise <= total_money_hypothesis:
    # check if the amount in the premise contradicts the estimate of more than 'total_money_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
