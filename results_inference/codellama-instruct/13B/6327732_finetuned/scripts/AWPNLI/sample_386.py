pears_keith_picked_premise = 47.0
pears_mike_picked_premise = 12.0
pears_keith_gave_away_premise = 46.0
pears_mike_left_hypothesis = 13.0

# the hypothesis refers to the number of pears left by Mike, which are also mentioned in the premise
# compute the total number of pears picked by both Keith and Mike
total_pears_picked_premise = pears_keith_picked_premise + pears_mike_picked_premise
# compute the total number of pears given away by Keith
total_pears_given_away_premise = pears_keith_gave_away_premise
# compute the total number of pears left by Mike
total_pears_left_premise = total_pears_picked_premise - total_pears_given_away_premise
if total_pears_left_premise!= pears_mike_left_hypothesis:
    # check if the number of pears left by Mike in the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
