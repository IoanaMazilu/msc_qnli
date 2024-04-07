# Premise: Aaron will jog from home at 3 miles per hour and then walk back home by the same route at 6 miles per hour.
# Hypothesis: Aaron will jog from home at less than 4 miles per hour and then walk back home by the same route at 6 miles per hour.
# Golden Label: entailment

jog_speed_premise = 3
jog_speed_hypothesis = 4
walk_speed_premise = 6
walk_speed_hypothesis = 6

# the hypothesis refers to the speeds of jogging and walking from home mentioned in the premise
if jog_speed_premise >= jog_speed_hypothesis:
    # check if the estimate of 'jog_speed_hypothesis' contradicts the jogging speed in the premise
    label = "contradiction"
elif walk_speed_hypothesis != walk_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speeds do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

