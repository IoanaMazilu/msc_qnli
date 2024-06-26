cats_premise = 17.0
gave_away_cats_premise = 14.0
cats_hypothesis = 5.0

# the hypothesis refers to the number of cats, which are also mentioned in the premise
# compute the remaining number of cats in the premise
remaining_cats_premise = cats_premise - gave_away_cats_premise
if cats_hypothesis!= remaining_cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of remaining cats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
