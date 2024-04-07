# Premise: Jack walks in a straight line toward Christina at a constant speed of 4 feet per second and Christina walks in a straight line toward Jack at a constant speed of 5 feet per second.
# Hypothesis: Jack walks in a straight line toward Christina at a constant speed of more than 1 feet per second and Christina walks in a straight line toward Jack at a constant speed of 5 feet per second.
# Golden Label: entailment

jack_speed_premise = 4
jack_speed_hypothesis = 1
christina_speed_premise = 5
christina_speed_hypothesis = 5

# the hypothesis refers to the walking speeds of Jack and Christina mentioned in the premise
if jack_speed_premise <= jack_speed_hypothesis:
    # check if the estimate of 'jack_speed_hypothesis' contradicts the speed of Jack in the premise
    label = "contradiction"
elif christina_speed_hypothesis != christina_speed_premise:
    # check if the speed of Christina in the hypothesis contradicts the speed of Christina reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
