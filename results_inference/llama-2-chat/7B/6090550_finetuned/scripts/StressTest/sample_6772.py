speed_AB_premise = 50
speed_BC_premise = 60
speed_AB_hypothesis = 40
speed_BC_hypothesis = 60

# the hypothesis refers to the speed at which Murali travelled from city A to city B and from city B to city C, as mentioned in the premise
if speed_AB_hypothesis >= speed_AB_premise:
    # check if the speed at which Murali travelled from city A to city B in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif speed_BC_hypothesis!= speed_BC_premise:
    # check if the speed at which Murali travelled from city B to city C in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
