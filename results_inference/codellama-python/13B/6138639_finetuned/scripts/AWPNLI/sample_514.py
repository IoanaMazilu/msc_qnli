birds_sitting_premise = 4.0
birds_flew_away_premise = 2.0
birds_sitting_hypothesis = 2.0

# the hypothesis refers to the number of birds sitting on the fence, which is also mentioned in the premise
# compute the number of birds sitting on the fence in the premise
birds_sitting_premise = birds_sitting_premise - birds_flew_away_premise
if birds_sitting_hypothesis!= birds_sitting_premise:
    # check if the number of birds sitting on the fence in the hypothesis contradicts the number of birds sitting on the fence from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
