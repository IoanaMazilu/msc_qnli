sacha_speed_premise = 7
bruno_speed_premise = 5
sacha_speed_hypothesis = 4
bruno_speed_hypothesis = 5

# the hypothesis contains both Sacha and Bruno's speed as mentioned in the premise
if sacha_speed_premise <= sacha_speed_hypothesis:
    # check if the premise speed of Sacha contradicts the lower bound in the hypothesis
    label = "contradiction"
elif bruno_speed_premise != bruno_speed_hypothesis:
    # check if Bruno's speed in the premise contradicts the amount specified in the hypothesis
    label = "contradiction"
else:
    # if both speeds from the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
