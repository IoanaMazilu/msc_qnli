liters_premise = 6522.0
liters_hypothesis = 1358.0

# the hypothesis refers to the amount of leaked oil, which is also mentioned in the premise
# compute the total amount of leaked oil from the premise
total_liters_leaked_premise = liters_premise - liters_hypothesis

# check if the number of leaked liters in the hypothesis contradicts the number of leaked liters from the premise
if total_liters_leaked_premise!= liters_hypothesis:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
