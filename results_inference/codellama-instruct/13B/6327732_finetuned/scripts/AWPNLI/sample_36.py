hamburgers_made_premise = 9.0
hamburgers_served_premise = 3.0
hamburgers_left_over_hypothesis = 6.0

# the hypothesis refers to the number of hamburgers left over, which are also mentioned in the premise
# compute the total number of hamburgers served from the premise
total_hamburgers_served_premise = hamburgers_made_premise - hamburgers_served_premise
if hamburgers_left_over_hypothesis!= total_hamburgers_served_premise:
    # check if the number of hamburgers left over from the hypothesis contradicts the number of hamburgers served from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
