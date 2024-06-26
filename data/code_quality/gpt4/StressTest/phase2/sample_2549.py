speed_A_B_premise = 40
speed_A_B_hypothesis = 40
speed_B_C_premise = 60
speed_B_C_hypothesis = 60

# the hypothesis talks about the speed of travel between cities A-B and B-C, referenced also in the premise
if speed_A_B_hypothesis > speed_A_B_premise:
    # check if the hypothesis value contradicts the stated speed of 'speed_A_B_premise' between cities A and B
    label = "contradiction"
elif speed_B_C_hypothesis != speed_B_C_premise:
    # check if the speed between cities B and C in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif speed_A_B_hypothesis == speed_A_B_premise:
    # if the speeds in the hypothesis exactly match the speeds in the premise, we can infer entailment
    label = "entailment"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, but also do not exactly match, we infer neutrality
    label = "neutral"

print(label)
