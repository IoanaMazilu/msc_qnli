amount_premise = 20000
months_premise = 7
amount_hypothesis = 20000
months_hypothesis = 6

# the hypothesis talks about the amount invested and the duration of investment, both mentioned in the premise
if amount_hypothesis!= amount_premise:
    # check if the amount in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
elif months_hypothesis >= months_premise:
    # check if the duration of investment in the hypothesis contradicts the duration of investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
