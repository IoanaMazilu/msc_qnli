birds_premise = 4.0
birds_flew_away_premise = 2.0
birds_hypothesis = 2.0

# the hypothesis refers to the number of birds, which are also mentioned in the premise
# compute the total number of birds in the premise
total_birds_premise = birds_premise - birds_flew_away_premise
if birds_hypothesis!= total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
