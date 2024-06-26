total_hamburgers_premise = 9.0
hot_dogs_premise = 4.0
extra_hamburgers_premise = 3.0
total_hamburgers_hypothesis = 12.0

# the hypothesis refers to the total number of hamburgers, which are also mentioned in the premise
# compute the total number of hamburgers in the premise
total_hamburgers_premise = total_hamburgers_premise + hot_dogs_premise

if total_hamburgers_hypothesis!= total_hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
