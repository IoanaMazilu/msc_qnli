speed_AB_premise = 30
speed_BC_premise = 60
speed_AB_hypothesis = 40
speed_BC_hypothesis = 60

# the hypothesis talks about Murali's travel speed from city A to city B and from city B to city C, which are also mentioned in the premise
if speed_AB_hypothesis <= speed_AB_premise:
    # check if the speed from city A to city B in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif speed_BC_hypothesis!= speed_BC_premise:
    # check if the speed from city B to city C in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)
