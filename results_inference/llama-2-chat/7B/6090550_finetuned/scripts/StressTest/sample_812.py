sacha_speed_premise = 6
bruno_speed_premise = 5
sacha_speed_hypothesis = 3
bruno_speed_hypothesis = 5

# the hypothesis refers to the speed of Sacha and Bruno mentioned in the premise
if sacha_speed_premise!= sacha_speed_hypothesis:
    # check if Sacha's speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if Bruno's speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
