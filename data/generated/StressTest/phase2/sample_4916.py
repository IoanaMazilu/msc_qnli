# Premise: If the average speed of the whole journey was 36 mph, then what is Tom's speed driving from B to C in miles per hour?
# Hypothesis: If the average speed of the whole journey was 26 mph, then what is Tom's speed driving from B to C in miles per hour?
# Golden Label: contradiction

average_speed_premise = 36
average_speed_hypothesis = 26

# the hypothesis talks about the average speed of the journey, which is also mentioned in the premise
if average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same average speed, so if they match, it's entailment
    label = "entailment"

print(label)

