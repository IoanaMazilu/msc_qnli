pears_jason_premise = 46.0
pears_keith_premise = 47.0
pears_mike_premise = 12.0
pears_left_hypothesis = 81.0

# the hypothesis refers to the number of pears left, which are also mentioned in the premise
# compute the total number of pears picked from the premise
total_pears_picked_premise = pears_jason_premise + pears_keith_premise
# compute the total number of pears eaten from the premise
total_pears_eaten_premise = pears_mike_premise
# compute the total number of pears left from the premise
total_pears_left_premise = total_pears_picked_premise - total_pears_eaten_premise
if total_pears_left_premise!= pears_left_hypothesis:
    # check if the number of pears left in the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
