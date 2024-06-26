premise = "What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 4:2?"
hypothesis = "What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 3:2?"

# extract the ratio of distances between A to B and B to C from the premise
ratio_premise = premise.split(":")[1]

# extract the ratio of distances between A to B and B to C from the hypothesis
ratio_hypothesis = hypothesis.split(":")[1]

# check if the ratio in the hypothesis contradicts the ratio in the premise
if ratio_hypothesis!= ratio_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
