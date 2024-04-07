# Premise: Murali travelled from city A to city B at a speed of 4 kmph and from city B to city C at 6 kmph.
# Hypothesis: Murali travelled from city A to city B at a speed of 1 kmph and from city B to city C at 6 kmph.
# Golden Label: contradiction

speed_AB_premise = 4
speed_BC_premise = 6
speed_AB_hypothesis = 1
speed_BC_hypothesis = 6

# the hypothesis speaks about Murali's travel speed between city A to B and B to C, also mentioned in the premise
if speed_AB_hypothesis != speed_AB_premise:
    # check if the speed from city A to B in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed from city B to C in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

