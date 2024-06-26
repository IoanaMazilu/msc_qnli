speed_fred_premise = 5
speed_sam_premise = 5
speed_fred_hypothesis = 8
speed_sam_hypothesis = 5

# the hypothesis refers to the speed of Fred and Sam, mentioned in the premise
if speed_fred_hypothesis <= speed_fred_premise:
    # check if the estimate of'speed_fred_hypothesis' contradicts the speed of Fred in the premise
    label = "contradiction"
elif speed_sam_hypothesis!= speed_sam_premise:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
