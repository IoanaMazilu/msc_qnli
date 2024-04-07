# Premise: Jack walks in a straight line toward Christina at a constant speed of more than 1 feet per second and Christina walks in a straight line toward Jack at a constant speed of 5 feet per second.
# Hypothesis: Jack walks in a straight line toward Christina at a constant speed of 4 feet per second and Christina walks in a straight line toward Jack at a constant speed of 5 feet per second.
# Golden Label: neutral

jack_speed_premise = 1
jack_speed_hypothesis = 4
christina_speed_premise = 5
christina_speed_hypothesis = 5

# the hypothesis talks about the speed of Jack and Christina, referenced also in the premise
if jack_speed_hypothesis <= jack_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jack_speed_premise'
    label = "contradiction"
elif christina_speed_hypothesis != christina_speed_premise:
    # check if the speed of Christina in the hypothesis contradicts the speed of Christina reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Jack
    # any speed of Jack greater than 'jack_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

