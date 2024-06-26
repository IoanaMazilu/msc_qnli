total_amount_premise = 6000
total_amount_hypothesis = 2000
ratio = [2, 4, 6]

# the hypothesis refers to the total amount shared among John, Jose & Binoy mentioned in the premise
if total_amount_premise <= total_amount_hypothesis:
    # check if the estimate of 'total_amount_hypothesis' contradicts the total amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
