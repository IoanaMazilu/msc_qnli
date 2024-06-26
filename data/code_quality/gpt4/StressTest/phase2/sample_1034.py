shirts_bought_premise = 160
shirts_bought_hypothesis = 360

# The hypothesis refers to the number of shirts bought by Vijay, also mentioned in the premise
if shirts_bought_premise != shirts_bought_hypothesis:
    # Check if the number of purchased shirts in the hypothesis contradicts the number of purchased shirts reported in the premise
    label = "contradiction"
else:
    # If the number of shirts bought in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
