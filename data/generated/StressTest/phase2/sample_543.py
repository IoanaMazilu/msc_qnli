# Premise: Between Tom in line 1 and Jack in line 2 there's a distance of 1.2 meters, the same as in the subsequent lanes.
# Hypothesis: Between Tom in line less than 6 and Jack in line 2 there's a distance of 1.2 meters, the same as in the subsequent lanes.
# Golden Label: entailment

tom_line_premise = 1
jack_line_premise = 2
distance_premise = 1.2

tom_line_hypothesis = 6
jack_line_hypothesis = 2
distance_hypothesis = 1.2

# the hypothesis refers to the same conditions as in the premise: the distance between two people (Tom and Jack) in different lanes
if tom_line_hypothesis > tom_line_premise:
    # check if 'tom_line_hypothesis' contradicts the line number of Tom in the premise
    label = "contradiction"
elif jack_line_hypothesis != jack_line_premise:
    # check if the line number of Jack in the hypothesis contradicts the line number of Jack in the premise
    label = "contradiction"
elif distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and conditions do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

