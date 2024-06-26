# the hypothesis refers to the number of sacks and the total number of pieces of wood gathered, which are also mentioned in the premise
# compute the total number of pieces of wood gathered from the premise
total_wood_premise = 80
# compute the number of sacks that can be filled with wood from the premise
sacks_premise = total_wood_premise / 20
if sacks_hypothesis!= sacks_premise:
    # check if the number of sacks from the hypothesis contradicts the number of sacks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
