pears_keith_premise = 47.0
pears_mike_premise = 12.0
pears_given_away_premise = 46.0
pears_mike_hypothesis = 13.0

# the hypothesis refers to the number of pears Mike has left, which can be computed from the premise
# compute the number of pears Mike has left in the premise
pears_mike_left_premise = pears_mike_premise - pears_given_away_premise
if pears_mike_hypothesis!= pears_mike_left_premise:
    # check if the number of pears Mike has left in the hypothesis contradicts the number of pears Mike has left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
