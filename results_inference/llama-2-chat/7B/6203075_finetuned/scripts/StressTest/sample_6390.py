sacha_speed_premise = 6
sacha_speed_hypothesis = 1
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the speed of Sacha and Bruno, which are also mentioned in the premise
if sacha_speed_premise <= sacha_speed_hypothesis:
    # check if the speed of Sacha in the hypothesis contradicts the speed of Sacha in the premise
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)