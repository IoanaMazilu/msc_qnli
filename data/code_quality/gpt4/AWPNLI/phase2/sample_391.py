found_seashells_premise = 56.0
given_seashells_premise = 22.0
total_seashells_hypothesis = 77.0

# the hypothesis refers to the total number of seashells, which are also mentioned in the premise
# compute the total number of seashells in the premise
total_seashells_premise = found_seashells_premise + given_seashells_premise
if total_seashells_hypothesis != total_seashells_premise:
    # check if the number of seashells in the hypothesis contradicts the number of seashells from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
