pears_picked_premise = 47.0
pears_picked_mike = 12.0
pears_given_away_premise = 46.0
pears_left_mike_hypothesis = 13.0

# the hypothesis refers to the number of pears left, which are also mentioned in the premise
# compute the number of pears left for Mike from the premise
pears_left_mike_premise = pears_picked_mike - pears_given_away_premise
if pears_left_mike_hypothesis!= pears_left_mike_premise:
    # check if the number of pears left for Mike in the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
