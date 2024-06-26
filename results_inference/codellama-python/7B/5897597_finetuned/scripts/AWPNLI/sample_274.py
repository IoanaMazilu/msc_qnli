roses_initial_premise = 37.0
roses_sold_premise = 16.0
roses_picked_premise = 19.0
total_roses_hypothesis = 40.0

# the hypothesis refers to the total number of roses, which are also mentioned in the premise
# compute the total number of roses in the premise
total_roses_premise = roses_initial_premise - roses_sold_premise + roses_picked_premise
if total_roses_hypothesis!= total_roses_premise:
    # check if the total number of roses in the hypothesis contradicts the total number of roses from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
