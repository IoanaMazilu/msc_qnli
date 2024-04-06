# Premise: Joan found 70.0 seashells on the beach and Sam gave her 27.0 seashells.
# Hypothesis: Joan has 92.0 seashells now.
# Golden Label: contradiction

found_seashells_premise = 70.0
given_seashells_premise = 27.0
total_seashells_hypothesis = 92.0

# the hypothesis refers to the total number of seashells, which are also mentioned in the premise
# compute the total number of seashells in the premise
total_seashells_premise = found_seashells_premise + given_seashells_premise
if total_seashells_hypothesis != total_seashells_premise:
    # check if the total number of seashells in the hypothesis contradicts the total number of seashells in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

