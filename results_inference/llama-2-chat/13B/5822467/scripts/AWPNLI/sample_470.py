hamburgers_premise = 9.0
hot_dogs_premise = 4.0
more_hamburgers_premise = 3.0
hamburgers_hypothesis = 12.0

# compute the total number of hamburgers and hot dogs served
total_hamburgers_premise = hamburgers_premise + more_hamburgers_premise
total_hot_dogs_premise = hot_dogs_premise

if hamburgers_hypothesis > total_hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers from the premise
    label = "contradiction"
elif hamburgers_hypothesis < total_hamburgers_premise:
    # check if the number of hamburgers in the hypothesis is less than the number of hamburgers from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
