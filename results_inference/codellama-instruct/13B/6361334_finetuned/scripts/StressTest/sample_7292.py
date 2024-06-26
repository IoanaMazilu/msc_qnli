total_amount_premise = 600
total_amount_hypothesis = 400
gregs_share_premise = 0
gregs_share_hypothesis = 0

# the hypothesis refers to the total amount and Greg's share mentioned in the premise
if total_amount_premise <= total_amount_hypothesis:
    # check if the estimate of 'total_amount_hypothesis' contradicts the total amount in the premise
    label = "contradiction"
elif gregs_share_hypothesis!= gregs_share_premise:
    # check if the share of Greg in the hypothesis contradicts the share of Greg in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
