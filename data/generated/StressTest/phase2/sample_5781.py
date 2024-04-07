# Premise: Lindy runs at a constant speed of 9 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Hypothesis: Lindy runs at a constant speed of more than 4 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Golden Label: entailment

lindy_speed_premise = 9
lindy_speed_hypothesis = 4

# the hypothesis refers to the same constant speed of Lindy as in the premise
if lindy_speed_hypothesis >= lindy_speed_premise:
    # check if the hypothesis speed contradicts Lindy's constant speed in the premise
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

