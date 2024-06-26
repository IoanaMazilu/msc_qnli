wood_per_sack_premise = 20.0
wood_hypothesis = 1600.0
sacks_hypothesis = 80.0

# the hypothesis refers to the number of pieces of firewood, which are also mentioned in the premise
# compute the total number of firewood in the hypothesis
total_wood_hypothesis = wood_per_sack_premise * sacks_hypothesis
if total_wood_hypothesis != wood_hypothesis:
    # check if the number of firewood in the hypothesis contradicts the number of firewood from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)