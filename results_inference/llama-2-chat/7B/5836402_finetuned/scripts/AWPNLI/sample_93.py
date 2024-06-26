total_eggs_premise = 47.0
taken_eggs_premise = 5.0
left_eggs_hypothesis = 41.0

# the hypothesis refers to the number of eggs, which are also mentioned in the premise
# compute the number of eggs left in the premise
left_eggs_premise = total_eggs_premise - taken_eggs_premise
if left_eggs_hypothesis!= left_eggs_premise:
    # check if the number of eggs left in the hypothesis contradicts the number of eggs left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
