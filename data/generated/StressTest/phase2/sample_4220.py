# Premise: Aaron will jog from home at 6 miles per hour and then walk back home by the same route at 12 miles per hour.
# Hypothesis: Aaron will jog from home at 2 miles per hour and then walk back home by the same route at 12 miles per hour.
# Golden Label: contradiction

jog_speed_premise = 6
jog_speed_hypothesis = 2
walk_speed_premise = 12
walk_speed_hypothesis = 12

# the hypothesis refers to the jogging and walking speeds mentioned in the premise
if jog_speed_premise != jog_speed_hypothesis:
    # check if the jogging speed in the hypothesis contradicts the jogging speed reported in the premise
    label = "contradiction"
elif walk_speed_premise != walk_speed_hypothesis:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

