# Premise: 2.0 beavers were working on their home and another 1.0 came to help.
# Hypothesis: 5.0 beavers are still working on their home.
# Golden Label: contradiction

working_beavers_premise = 2.0
joined_beavers_premise = 1.0
total_beavers_hypothesis = 5.0

# the hypothesis refers to the number of beavers, which are also mentioned in the premise
# compute the total number of beavers in the premise
total_beavers_premise = working_beavers_premise + joined_beavers_premise
if total_beavers_hypothesis != total_beavers_premise:
    # check if the number of beavers in the hypothesis contradicts the number of beavers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

