# Premise: Lindy runs at a constant speed of 10 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Hypothesis: Lindy runs at a constant speed of more than 10 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Golden Label: contradiction

lindy_speed_premise = 10
lindy_speed_hypothesis = 10

# the hypothesis refers to Lindy's running speed mentioned in the premise
if lindy_speed_hypothesis <= lindy_speed_premise:
    # check if the speed value in the hypothesis contradicts the speed value in the premise
    label = "contradiction"
elif lindy_speed_hypothesis > lindy_speed_premise:
    # check if the speed value in the hypothesis is greater than the speed value in the premise
    label = "contradiction"
else:
    # if the speed value in the hypothesis matches the speed value in the premise, we can infer entailment
    label = "entailment"

print(label)
