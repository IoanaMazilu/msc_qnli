sacha_speed_premise = 6
bruno_speed_premise = 5
sacha_speed_hypothesis = 3
bruno_speed_hypothesis = 5

# the hypothesis refers to the speed of Sacha and Bruno, as mentioned in the premise
if sacha_speed_premise!= sacha_speed_hypothesis:
    # check if Sacha's speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if Bruno's speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)
