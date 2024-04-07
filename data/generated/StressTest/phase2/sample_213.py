# Premise: If the average speed of the whole journey was 36 mph, then what is Tom's speed driving from B to C in miles per hour?
# Hypothesis: If the average speed of the whole journey was less than 76 mph, then what is Tom's speed driving from B to C in miles per hour?
# Golden Label: entailment

average_speed_premise = 36
average_speed_hypothesis = 76

# the hypothesis refers to the average speed of the journey mentioned in the premise
if average_speed_premise >= average_speed_hypothesis:
    # check if the estimate of 'average_speed_hypothesis' contradicts the average speed of the journey in the premise
    label = "contradiction"
else:
    # if the average speed of the journey in the premise is less than 'average_speed_hypothesis', we can infer entailment
    label = "entailment"

print(label)

