# Premise: Alyssa picked 25.0 limes, and Mike picked 32.0 limes and Tom picked 12.0 plums.
# Hypothesis: 57.0 limes were picked in all.
# Golden Label: entailment

alyssa_limes_premise = 25.0
mike_limes_premise = 32.0
total_limes_hypothesis = 57.0

# the hypothesis refers to the total number of limes, which are also mentioned in the premise
# compute the total number of limes in the premise
total_limes_premise = alyssa_limes_premise + mike_limes_premise
if total_limes_hypothesis != total_limes_premise:
    # check if the total number of limes in the hypothesis contradicts the total number of limes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

