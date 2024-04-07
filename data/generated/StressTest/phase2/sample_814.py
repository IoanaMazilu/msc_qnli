# Premise: Murali travelled from city A to city B at a speed of more than 30 kmph and from city B to city C at 60 kmph.
# Hypothesis: Murali travelled from city A to city B at a speed of 40 kmph and from city B to city C at 60 kmph.
# Golden Label: neutral

speed_AB_premise = 30
speed_AB_hypothesis = 40
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis talks about the travel speed between cities A to B and B to C, mentioned also in the premise
if speed_AB_hypothesis <= speed_AB_premise:
    # check if the hypothesis value contradicts the estimate of more than 'speed_AB_premise'
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed between cities B and C in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed between cities A and B
    # any speed greater than 'speed_AB_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

