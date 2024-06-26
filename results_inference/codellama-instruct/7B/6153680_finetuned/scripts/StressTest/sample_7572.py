speed_fred_premise = 2
speed_sam_premise = 5
speed_fred_hypothesis = 7
speed_sam_hypothesis = 5

# the hypothesis refers to the speed of Fred and Sam mentioned in the premise
if speed_fred_hypothesis <= speed_fred_premise and speed_sam_hypothesis == speed_sam_premise:
    # check if the speeds in the hypothesis contradict the speeds in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
