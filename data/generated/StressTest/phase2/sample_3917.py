# Premise: Lindy runs at a constant speed of 12 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Hypothesis: Lindy runs at a constant speed of 22 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Golden Label: contradiction

running_speed_premise = 12
running_speed_hypothesis = 22

# the hypothesis refers to Lindy's running speed, which is also mentioned in the premise
if running_speed_hypothesis != running_speed_premise:
    # check if the running speed in the hypothesis contradicts the running speed reported in the premise
    label = "contradiction"
else:
    # if the running speed in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

