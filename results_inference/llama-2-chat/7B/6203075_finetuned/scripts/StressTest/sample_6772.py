speed_AB_premise = 50
speed_BC_premise = 60
speed_AB_hypothesis = 40
speed_BC_hypothesis = 60

# the hypothesis talks about the speed of Murali's travel from city A to city B and from city B to city C
if speed_AB_hypothesis >= speed_AB_premise:
    # check if the speed of travel from city A to city B in the hypothesis contradicts the premise
    label = "contradiction"
elif speed_BC_hypothesis!= speed_BC_premise:
    # check if the speed of travel from city B to city C in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
