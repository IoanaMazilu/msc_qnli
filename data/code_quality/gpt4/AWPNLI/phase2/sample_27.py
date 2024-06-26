pears_picked_alyssa_premise = 42.0
pears_picked_nancy_premise = 17.0
total_pears_picked_hypothesis = 60.0

# the hypothesis refers to the total number of pears picked, which is also mentioned in the premise
# compute the total number of pears picked in the premise
total_pears_picked_premise = pears_picked_alyssa_premise + pears_picked_nancy_premise
if total_pears_picked_hypothesis != total_pears_picked_premise:
    # check if the total number of pears picked in the hypothesis contradicts the total number of pears picked from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
