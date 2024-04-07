# Premise: Aaron will jog from home at less than 7 miles per hour and then walk back home by the same route at 4 miles per hour.
# Hypothesis: Aaron will jog from home at 2 miles per hour and then walk back home by the same route at 4 miles per hour.
# Golden Label: neutral

jog_speed_premise = 7
jog_speed_hypothesis = 2
walk_speed_premise = 4
walk_speed_hypothesis = 4

# the hypothesis refers to the speed of jogging and walking mentioned in the premise
if jog_speed_hypothesis >= jog_speed_premise:
    # check if the 'jog_speed_hypothesis' contradicts the speed of jogging in the premise
    label = "contradiction"
elif walk_speed_hypothesis != walk_speed_premise:
    # check if the speed of walking in the hypothesis contradicts the speed of walking in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

