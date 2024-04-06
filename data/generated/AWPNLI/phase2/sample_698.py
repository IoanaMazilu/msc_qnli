# Premise: Mike had 34.0 peaches left at his roadside fruit stand and he went to the orchard and picked 86.0 more peaches to stock up the stand.
# Hypothesis: He has 120.0 peaches now.
# Golden Label: entailment

peaches_left_premise = 34.0
picked_peaches_premise = 86.0
peaches_hypothesis = 120.0

# the hypothesis refers to the total number of peaches, which is discussed in the premise
# calculate the total number of peaches from the premise
total_peaches_premise = peaches_left_premise + picked_peaches_premise
if peaches_hypothesis != total_peaches_premise:
    # check if the total number of peaches in the hypothesis contradicts the total number of peaches from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

