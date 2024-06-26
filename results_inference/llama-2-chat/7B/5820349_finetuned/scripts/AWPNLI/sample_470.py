hamburgers_made_premise = 9.0
hot_dogs_made_premise = 4.0
hamburgers_made_additional_premise = 3.0
total_hamburgers_hypothesis = 12.0

# the hypothesis refers to the total number of hamburgers made, which are also mentioned in the premise
# compute the total number of hamburgers made in the premise
total_hamburgers_premise = hamburgers_made_premise + hot_dogs_made_premise + hamburgers_made_additional_premise
if total_hamburgers_hypothesis!= total_hamburgers_premise:
    # check if the total number of hamburgers in the hypothesis contradicts the total number of hamburgers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
