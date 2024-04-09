initial_roses_premise = 37.0
sold_roses_premise = 16.0
picked_roses_premise = 19.0
total_roses_hypothesis = 40.0

# the hypothesis refers to the total number of roses, which is also mentioned in the premise
# compute the total number of roses in the premise
total_roses_premise = initial_roses_premise - sold_roses_premise + picked_roses_premise
if total_roses_hypothesis!= total_roses_premise:
    # check if the number of roses in the hypothesis contradicts the number of roses from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
