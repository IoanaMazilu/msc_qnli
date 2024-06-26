hamburgers_made_premise = 9.0
hot_dogs_made_premise = 4.0
hamburgers_made_addition_premise = 3.0
hamburgers_made_hypothesis = 12.0

# the hypothesis refers to the number of hamburgers made, which is also mentioned in the premise
# compute the total number of hamburgers made in the premise
total_hamburgers_made_premise = hamburgers_made_premise + hamburgers_made_addition_premise
if hamburgers_made_hypothesis!= total_hamburgers_made_premise:
    # check if the number of hamburgers made in the hypothesis contradicts the number of hamburgers made from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
