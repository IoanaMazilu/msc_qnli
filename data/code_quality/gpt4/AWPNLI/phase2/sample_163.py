dogs_premise = 2.0
biscuits_per_dog_premise = 3.0
total_biscuits_hypothesis = 9.0

# the hypothesis refers to the total number of biscuits, which are also mentioned in the premise
# compute the total number of biscuits in the premise
total_biscuits_premise = dogs_premise * biscuits_per_dog_premise
if total_biscuits_hypothesis != total_biscuits_premise:
    # check if the total number of biscuits in the hypothesis contradicts the total number of biscuits from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
