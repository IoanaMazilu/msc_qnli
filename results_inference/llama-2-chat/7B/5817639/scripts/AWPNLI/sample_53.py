black_lambs_premise = 193
white_lambs_premise = 193
total_lambs_hypothesis = 5854

# compare the number of black lambs in the hypothesis with the number of white lambs in the premise
if total_lambs_hypothesis - black_lambs_premise!= 0:
    # if the number of black lambs in the hypothesis is not equal to the number of white lambs in the premise, we have a contradiction
    label = "contradiction"
elif total_lambs_hypothesis - black_lambs_premise < 0:
    # if the number of black lambs in the hypothesis is less than the number of white lambs in the premise, we have entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we have neither entailment nor contradiction
    label = "neutral"

print(label)
