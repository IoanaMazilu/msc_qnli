pears_keith_picked_premise = 47.0
pears_mike_picked_premise = 12.0
pears_keith_gave_away_premise = 46.0
pears_mike_left_hypothesis = 13.0

# the hypothesis refers to the number of pears Mike has left, which are also mentioned in the premise
# compute the total number of pears Mike picked from the premise
total_pears_mike_picked_premise = pears_keith_picked_premise + pears_mike_picked_premise - pears_keith_gave_away_premise
if pears_mike_left_hypothesis!= total_pears_mike_picked_premise:
    # check if the number of pears left in the hypothesis contradicts the number of pears Mike picked from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
