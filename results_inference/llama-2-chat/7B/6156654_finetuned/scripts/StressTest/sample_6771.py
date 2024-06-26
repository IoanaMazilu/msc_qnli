speed_from_A_to_B_premise = 40
speed_from_B_to_C_premise = 60
speed_from_A_to_B_hypothesis = 50

# the hypothesis talks about the speed from city A to city B and from city B to city C, which are also mentioned in the premise
if speed_from_A_to_B_premise >= speed_from_A_to_B_hypothesis:
    # check if the speed from city A to city B in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_from_B_to_C_premise!= 60:
    # check if the speed from city B to city C in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
