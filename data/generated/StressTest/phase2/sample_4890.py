# Premise: If the average speed of the whole journey was 36 mph, then what is Tom's speed driving from B to C in miles per hour?
# Hypothesis: If the average speed of the whole journey was less than 46 mph, then what is Tom's speed driving from B to C in miles per hour?
# Golden Label: entailment

avg_speed_premise = 36
avg_speed_hypothesis = 46

# the hypothesis and premise both talk about the average speed of the whole journey
if avg_speed_hypothesis <= avg_speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif avg_speed_hypothesis != avg_speed_premise:
    # check if the speed in the hypothesis is not equal to the speed in the premise
    label = "neutral"
else:
    # if the speeds match exactly, we can infer entailment
    label = "entailment"

print(label)

