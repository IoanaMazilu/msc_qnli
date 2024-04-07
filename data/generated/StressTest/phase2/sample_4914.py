# Premise: If the average speed of the whole journey was 36 mph, then what is Tom's speed driving from B to C in miles per hour?
# Hypothesis: If the average speed of the whole journey was less than 56 mph, then what is Tom's speed driving from B to C in miles per hour?
# Golden Label: entailment

avg_speed_premise = 36
avg_speed_hypothesis = 56

# the hypothesis refers to the average speed of a journey mentioned in the premise
if avg_speed_hypothesis <= avg_speed_premise:
    # check if the value in 'avg_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
elif avg_speed_premise != avg_speed_hypothesis:
    # if the average speeds mentioned in premise and hypothesis are different, it means there is no explicit entailment
    label = "neutral"
else:
    # if the average speeds in the premise and hypothesis are the same, then we can infer entailment
    label = "entailment"

print(label)

