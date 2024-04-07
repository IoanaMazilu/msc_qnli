# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 4:2?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is more than 1:2?
# Golden Label: entailment

distance_ratio_premise = 4 / 2
distance_ratio_hypothesis = 1 / 2

# the hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if distance_ratio_premise <= distance_ratio_hypothesis:
    # check if the 'distance_ratio_hypothesis' contradicts the ratio of distances in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

