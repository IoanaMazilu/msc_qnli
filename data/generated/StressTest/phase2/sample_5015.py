# Premise: Jack walks in a straight line toward Christina at a constant speed of 4 feet per second and Christina walks in a straight line toward Jack at a constant speed of 5 feet per second.
# Hypothesis: Jack walks in a straight line toward Christina at a constant speed of 6 feet per second and Christina walks in a straight line toward Jack at a constant speed of 5 feet per second.
# Golden Label: contradiction

jack_speed_premise = 4
jack_speed_hypothesis = 6
christina_speed_premise = 5
christina_speed_hypothesis = 5

# the hypothesis talks about the walking speed of Jack and Christina, which is also mentioned in the premise
if jack_speed_hypothesis != jack_speed_premise:
    # check if Jack's walking speed in the hypothesis contradicts his speed mentioned in the premise
    label = "contradiction"
elif christina_speed_hypothesis != christina_speed_premise:
    # check if Christina's walking speed in the hypothesis contradicts her speed mentioned in the premise
    label = "contradiction"
else:
    # if all the speeds in the hypothesis match with the speeds mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
