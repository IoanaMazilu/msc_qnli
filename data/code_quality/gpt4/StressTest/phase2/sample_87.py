deposit_premise = 67600
deposit_hypothesis = 27600
annual_return_premise = 16
annual_return_hypothesis = 16

# the hypothesis refers to the deposit and annual return rate mentioned in the premise
if deposit_premise <= deposit_hypothesis:
    # check if the value 'deposit_hypothesis' contradicts the deposit amount in the premise
    label = "contradiction"
elif annual_return_hypothesis != annual_return_premise:
    # check if the annual return rate in the hypothesis contradicts the annual return rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
