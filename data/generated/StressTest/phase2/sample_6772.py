# Premise: Murali travelled from city A to city B at a speed of less than 50 kmph and from city B to city C at 60 kmph.
# Hypothesis: Murali travelled from city A to city B at a speed of 40 kmph and from city B to city C at 60 kmph.
# Golden Label: neutral

speed_A_to_B_premise = 50
speed_A_to_B_hypothesis = 40
speed_B_to_C_premise = 60
speed_B_to_C_hypothesis = 60

# the hypothesis talks about the speed of travel between cities A to B and B to C, mentioned also in the premise
if speed_A_to_B_hypothesis >= speed_A_to_B_premise:
    # check if the speed of travel from city A to B in the hypothesis contradicts the premise estimate
    label = "contradiction"
elif speed_B_to_C_hypothesis != speed_B_to_C_premise:
    # check if the speed of travel from city B to C in the hypothesis contradicts the premise value
    label = "contradiction"
else:
    # the premise provides an estimate for the speed of travel from city A to B and an exact value for city B to C
    # if the speed values in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

