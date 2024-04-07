# Premise: If the average speed of the whole journey was 36 mph, then what is Tom's speed driving from B to C in miles per hour?
# Hypothesis: If the average speed of the whole journey was more than 16 mph, then what is Tom's speed driving from B to C in miles per hour?
# Golden Label: entailment

average_speed_premise = 36
average_speed_hypothesis = 16

# the hypothesis refers to the average speed of the whole journey mentioned in the premise
if average_speed_premise <= average_speed_hypothesis:
    # check if 'average_speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

