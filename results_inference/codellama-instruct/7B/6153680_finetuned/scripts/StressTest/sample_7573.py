speed_fred_premise = 7
speed_sam_premise = 5
speed_fred_hypothesis = 2
speed_sam_hypothesis = 5

# the hypothesis refers to the same scenario as the premise, but with different speeds
if speed_fred_hypothesis >= speed_fred_premise and speed_sam_hypothesis == speed_sam_premise:
    # check if the speeds in the hypothesis contradict the speeds in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)
