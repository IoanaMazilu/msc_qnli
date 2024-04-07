# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 4:2?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 3:2?
# Golden Label: contradiction

ratio_distance_premise = [4, 2]
ratio_distance_hypothesis = [3, 2]

# The hypothesis talks about the ratio of distances from A to B and B to C, just like the premise
if ratio_distance_premise != ratio_distance_hypothesis:
    # If the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # If the ratio in the hypothesis doesn't contradict the ratio in the premise, it's neutral because we can't infer anything else
    label = "neutral"

print(label)

