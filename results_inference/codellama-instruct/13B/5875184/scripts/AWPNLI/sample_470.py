premise_hamburgers = 9.0
premise_hot_dogs = 4.0
hypothesis_hamburgers = 12.0

# the hypothesis refers to the total number of hamburgers made, which is also mentioned in the premise
# compute the total number of hamburgers made during lunch
total_hamburgers_premise = premise_hamburgers + premise_hot_dogs
if hypothesis_hamburgers > total_hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers made during lunch
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
