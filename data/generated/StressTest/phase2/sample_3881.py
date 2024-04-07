# Premise: Aaron will jog from home at 2 miles per hour and then walk back home by the same route at 4 miles per hour.
# Hypothesis: Aaron will jog from home at more than 2 miles per hour and then walk back home by the same route at 4 miles per hour.
# Golden Label: contradiction

jog_speed_premise = 2
jog_speed_hypothesis = 2
walk_speed_premise = 4
walk_speed_hypothesis = 4

# the hypothesis refers to Aaron's jogging and walking speeds mentioned in the premise
if jog_speed_hypothesis <= jog_speed_premise:
    # check if the 'jog_speed_hypothesis' contradicts the jogging speed in the premise
    label = "contradiction"
elif walk_speed_hypothesis != walk_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speeds do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

