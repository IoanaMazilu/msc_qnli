wood_per_sack_premise = 20.0
sacks_filled_hypothesis = 6.0
total_wood_gathered_hypothesis = 80.0

# the hypothesis refers to the number of sacks filled and total wood gathered, which are also mentioned in the premise
# compute the total number of sacks filled in the premise
sacks_filled_premise = wood_per_sack_premise / wood_per_sack_premise
if sacks_filled_hypothesis!= round(sacks_filled_premise * total_wood_gathered_hypothesis, 2):
    # check if the number of sacks filled in the hypothesis contradicts the number of sacks filled from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
