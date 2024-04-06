# Premise: 2.0 beavers were working on their home and 1.0 went for a swim.
# Hypothesis: 0.0 beavers are still working on their home.
# Golden Label: contradiction

working_beavers_premise = 2.0
swimming_beavers_premise = 1.0
working_beavers_hypothesis = 0.0

# the hypothesis refers to the number of beavers working, which is also mentioned in the premise
# compute the number of beavers still working in the premise
remaining_beavers_premise = working_beavers_premise - swimming_beavers_premise
if working_beavers_hypothesis != remaining_beavers_premise:
    # check if the number of working beavers in the hypothesis contradicts the number of remaining beavers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

