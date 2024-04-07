# Premise: Jack walks in a straight line toward Christina at a constant speed of less than 6 feet per second and Christina walks in a straight line toward Jack at a constant speed of 3 feet per second.
# Hypothesis: Jack walks in a straight line toward Christina at a constant speed of 5 feet per second and Christina walks in a straight line toward Jack at a constant speed of 3 feet per second.
# Golden Label: neutral

jack_speed_premise = 6
jack_speed_hypothesis = 5
christina_speed_premise = 3
christina_speed_hypothesis = 3

# the hypothesis refers to the speeds of Jack and Christina mentioned in the premise
if jack_speed_hypothesis >= jack_speed_premise:
    # check if the 'jack_speed_hypothesis' contradicts the speed of Jack in the premise
    label = "contradiction"
elif christina_speed_hypothesis != christina_speed_premise:
    # check if the speed of Christina in the hypothesis contradicts the speed of Christina reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

