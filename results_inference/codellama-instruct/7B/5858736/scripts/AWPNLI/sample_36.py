hamburgers_made_premise = 9.0
hamburgers_served_premise = 3.0
hamburgers_left_over_hypothesis = 6.0

# the hypothesis refers to the number of hamburgers left over, which are also mentioned in the premise
# compute the number of hamburgers served from the premise
hamburgers_served_premise = hamburgers_made_premise - hamburgers_left_over_hypothesis
if hamburgers_served_premise!= 0:
    # check if the number of hamburgers served from the premise is not zero
    label = "entailment"
else:
    # if the number of hamburgers served from the premise is zero, we can infer contradiction
    label = "contradiction"

print(label)
