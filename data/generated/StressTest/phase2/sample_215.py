# Premise: If the average speed of the whole journey was 36 mph, then what is Tom's speed driving from B to C in miles per hour?
# Hypothesis: If the average speed of the whole journey was less than 36 mph, then what is Tom's speed driving from B to C in miles per hour?
# Golden Label: contradiction

average_speed_premise = 36
average_speed_hypothesis = 36

# the hypothesis refers to the average speed of the journey mentioned in the premise
if average_speed_hypothesis < average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the average speed in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

