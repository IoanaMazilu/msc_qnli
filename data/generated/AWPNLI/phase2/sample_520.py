# Premise: 2.0 beavers were working on their home and another 1.0 came to help.
# Hypothesis: 3.0 beavers are still working on their home.
# Golden Label: entailment

beavers_working_premise = 2.0
beavers_came_premise = 1.0
beavers_working_hypothesis = 3.0

# the hypothesis refers to the number of beavers, which are also mentioned in the premise
# compute the total number of beavers in the premise
total_beavers_premise = beavers_working_premise + beavers_came_premise

if beavers_working_hypothesis != total_beavers_premise:
    # check if the number of beavers in the hypothesis contradicts the number of beavers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

