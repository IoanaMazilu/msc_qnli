hamburgers_lunch_premise = 9.0
hot_dogs_lunch_premise = 4.0
hamburgers_addition_premise = 3.0
hamburgers_hypothesis = 12.0

# the hypothesis refers to the number of hamburgers made, which are also mentioned in the premise
# compute the total number of hamburgers made during lunch
total_hamburgers_lunch = hamburgers_lunch_premise + hamburgers_addition_premise
if hamburgers_hypothesis!= total_hamburgers_lunch:
    # check if the number of hamburgers made in the hypothesis contradicts the number of hamburgers made during lunch
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
