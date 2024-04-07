# Premise: Lindy runs at a constant speed of 8 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Hypothesis: Lindy runs at a constant speed of more than 1 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Golden Label: entailment

speed_premise = 8
speed_hypothesis = 1

# the hypothesis refers to the speed of Lindy mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis speed contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # if the hypothesis speed is less than the premise speed, we can infer entailment
    label = "entailment"

print(label)

