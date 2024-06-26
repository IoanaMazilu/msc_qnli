rubys_premise = 5155.0
diamonds_premise = 45.0
total_gems_hypothesis = 5200.0

# the hypothesis refers to the total number of gems, which are also mentioned in the premise
# compute the total number of gems in the premise
total_gems_premise = rubys_premise + diamonds_premise
if total_gems_hypothesis != total_gems_premise:
    # check if the number of gems in the hypothesis contradicts the number of gems from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
