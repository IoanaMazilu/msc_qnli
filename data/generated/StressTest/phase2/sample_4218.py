# Premise: Aaron will jog from home at 6 miles per hour and then walk back home by the same route at 12 miles per hour.
# Hypothesis: Aaron will jog from home at more than 4 miles per hour and then walk back home by the same route at 12 miles per hour.
# Golden Label: entailment

jog_speed_premise = 6
jog_speed_hypothesis = 4
walk_speed_premise = 12
walk_speed_hypothesis = 12

# the hypothesis refers to the speed of jogging and walking mentioned in the premise
if jog_speed_premise <= jog_speed_hypothesis:
    # check if the estimate of 'jog_speed_hypothesis' contradicts the jog speed in the premise
    label = "contradiction"
elif walk_speed_hypothesis != walk_speed_premise:
    # check if the walk speed in the hypothesis contradicts the walk speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

