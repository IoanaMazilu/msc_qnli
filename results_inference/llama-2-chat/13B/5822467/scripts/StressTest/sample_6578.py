shirt_cost_premise = Rs.160
shirt_cost_hypothesis = Rs.100

# the hypothesis refers to the number of shirts and their cost mentioned in the premise
if shirt_cost_premise <= shirt_cost_hypothesis:
    # check if the estimate of'shirt_cost_hypothesis' contradicts the cost of shirts in the premise
    label = "contradiction"
elif shirt_cost_hypothesis!= shirt_cost_premise:
    # check if the cost of shirts in the hypothesis contradicts the cost of shirts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
