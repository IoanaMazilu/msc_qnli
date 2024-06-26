abhay_speed_premise = 1
abhay_speed_hypothesis = 8

# the hypothesis refers to the time difference between Abhay and Sammer if Abhay doubles his speed, similar to the premise
if abhay_speed_hypothesis != abhay_speed_premise:
    # check if the time difference in the hypothesis contradicts the time difference mentioned in the premise
    label = "contradiction"
else:
    # if the time difference in the hypothesis and premise are the same, then we can infer entailment
    label = "entailment"

print(label)
