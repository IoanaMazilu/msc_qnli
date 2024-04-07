# Premise: Jack walks in a straight line toward Christina at a constant speed of less than 8 feet per second and Christina walks in a straight line toward Jack at a constant speed of 8 feet per second.
# Hypothesis: Jack walks in a straight line toward Christina at a constant speed of 7 feet per second and Christina walks in a straight line toward Jack at a constant speed of 8 feet per second.
# Golden Label: neutral

jack_speed_premise = 8
jack_speed_hypothesis = 7
christina_speed_premise = 8
christina_speed_hypothesis = 8

# the hypothesis refers to the speed at which Jack and Christina are walking towards each other, mentioned also in the premise
if jack_speed_hypothesis >= jack_speed_premise:
    # check if the speed of Jack in the hypothesis contradicts the premise of him walking slower than 'jack_speed_premise'
    label = "contradiction"
elif christina_speed_hypothesis != christina_speed_premise:
    # check if the speed of Christina in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

