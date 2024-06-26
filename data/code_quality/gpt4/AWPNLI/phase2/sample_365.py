found_seashells_premise = 8.0
gave_seashells_premise = 6.0
left_seashells_hypothesis = 1.0

# the hypothesis refers to the number of seashells left with Jessica, which can be computed from the premise
# compute the number of seashells left with Jessica in the premise
left_seashells_premise = found_seashells_premise - gave_seashells_premise
if left_seashells_hypothesis != left_seashells_premise:
    # check if the number of seashells left in the hypothesis contradicts the number of seashells left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
