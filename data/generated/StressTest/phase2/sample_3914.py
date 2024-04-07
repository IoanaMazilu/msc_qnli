# Premise: Jack walks in a straight line toward Christina at a constant speed of 5 feet per second and Christina walks in a straight line toward Jack at a constant speed of 7 feet per second.
# Hypothesis: Jack walks in a straight line toward Christina at a constant speed of 4 feet per second and Christina walks in a straight line toward Jack at a constant speed of 7 feet per second.
# Golden Label: contradiction

jack_speed_premise = 5
jack_speed_hypothesis = 4
christina_speed_premise = 7
christina_speed_hypothesis = 7

# the hypothesis talks about the speed of both Jack and Christina, referenced also in the premise
if jack_speed_hypothesis != jack_speed_premise:
    # check if the speed of Jack in the hypothesis contradicts the speed of Jack mentioned in the premise
    label = "contradiction"
elif christina_speed_hypothesis != christina_speed_premise:
    # check if the speed of Christina in the hypothesis contradicts the speed of Christina mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

