lunch_cakes_premise = 5.0
dinner_cakes_premise = 6.0
total_cakes_hypothesis = 14.0

# the hypothesis refers to the total number of cakes, which is also mentioned in the premise
if total_cakes_hypothesis!= (lunch_cakes_premise + dinner_cakes_premise):
    # check if the total number of cakes in the hypothesis contradicts the total number of cakes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
