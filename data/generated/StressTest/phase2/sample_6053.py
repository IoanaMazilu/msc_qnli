# Premise: Aaron will jog from home at 3 miles per hour and then walk back home by the same route at 6 miles per hour.
# Hypothesis: Aaron will jog from home at 7 miles per hour and then walk back home by the same route at 6 miles per hour.
# Golden Label: contradiction

jog_speed_premise = 3
jog_speed_hypothesis = 7
walk_speed_premise = 6
walk_speed_hypothesis = 6

# the hypothesis refers to the speed of jogging and walking mentioned in the premise
if jog_speed_hypothesis != jog_speed_premise:
    # check if the jogging speed in the hypothesis contradicts the jogging speed reported in the premise
    label = "contradiction"
elif walk_speed_hypothesis != walk_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

