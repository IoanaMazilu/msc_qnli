sitting_birds_premise = 21.0 
flew_away_birds_premise = 14.0
left_birds_hypothesis = 6.0

# the hypothesis refers to the number of birds left in the tree, which can be estimated from the premise
# compute the number of birds left in the tree in the premise
left_birds_premise = sitting_birds_premise - flew_away_birds_premise
if left_birds_hypothesis != left_birds_premise:
    # check if the number of birds left in the tree in the hypothesis contradicts the number of birds left in the tree from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
