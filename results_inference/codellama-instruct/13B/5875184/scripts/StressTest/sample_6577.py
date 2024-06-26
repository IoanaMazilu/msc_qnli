premise_shirts = 560
hypothesis_shirts = 160
premise_rate = 0
hypothesis_rate = 0

# the hypothesis refers to the number of shirts and rate mentioned in the premise
if hypothesis_shirts <= premise_shirts:
    # check if the estimate of 'hypothesis_shirts' contradicts the number of shirts in the premise
    label = "contradiction"
elif hypothesis_rate!= premise_rate:
    # check if the rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
