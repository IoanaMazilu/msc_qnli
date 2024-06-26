pears_jason_premise = 46.0
pears_keith_premise = 47.0
pears_mike_premise = 12.0
pears_hypothesis = 81.0

# the hypothesis refers to the total number of pears, which are also mentioned in the premise
# compute the total number of pears picked by Jason and Keith
total_pears_picked_premise = pears_jason_premise + pears_keith_premise
# compute the total number of pears eaten by Mike
total_pears_eaten_premise = pears_mike_premise
# compute the total number of pears left
total_pears_left_premise = total_pears_picked_premise - total_pears_eaten_premise
if total_pears_hypothesis!= total_pears_left_premise:
    # check if the number of pears in the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
