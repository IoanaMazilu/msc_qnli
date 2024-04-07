# Premise: Murali travelled from city A to city B at a speed of 40 kmph and from city B to city C at 60 kmph.
# Hypothesis: Murali travelled from city A to city B at a speed of more than 40 kmph and from city B to city C at 60 kmph.
# Golden Label: contradiction

speed_AB_premise = 40
speed_AB_hypothesis = 40
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis mentions Murali's speed from city A to city B and from city B to city C as stated in the premise
if speed_AB_hypothesis <= speed_AB_premise:
    # check if the hypothesis estimate contradicts the speed from city A to city B stated in the premise
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed from city B to city C stated in the hypothesis contradicts the speed from city B to city C stated in the premise
    label = "contradiction"
else:
    # if the hypothesis estimates and values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

