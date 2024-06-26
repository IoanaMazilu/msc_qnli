hamburgers_premise = 9.0
hot_dogs_premise = 4.0
hamburgers_made_later_premise = 3.0
hamburgers_hypothesis = 12.0

# the hypothesis refers to the number of hamburgers made, which are also mentioned in the premise
# compute the total number of hamburgers made during lunch
total_hamburgers_premise = hamburgers_premise + hot_dogs_premise
if hamburgers_hypothesis!= total_hamburgers_premise + hamburgers_made_later_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers made during lunch and later
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
