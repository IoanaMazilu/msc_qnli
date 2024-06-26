limes_premise = 25
limes_mike_premise = 32
limes_tom_premise = 12
total_limes_hypothesis = 61

# the hypothesis refers to the total number of limes, which are also mentioned in the premise
# compute the total number of limes from the premise
total_limes_premise = limes_premise + limes_mike_premise + limes_tom_premise
if total_limes_hypothesis!= total_limes_premise:
    # check if the number of limes in the hypothesis contradicts the number of limes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
