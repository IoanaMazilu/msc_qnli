speed_from_a_to_b_premise = 40
speed_from_b_to_c_premise = 60
speed_less_than_50_hypothesis = 50

# the hypothesis refers to the speed of travel from city A to city B and from city B to city C
if speed_from_a_to_b_premise >= speed_less_than_50_hypothesis:
    # check if the speed of travel from city A to city B in the premise contradicts the hypothesis
    label = "contradiction"
elif speed_from_b_to_c_premise!= 60:
    # check if the speed of travel from city B to city C in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
