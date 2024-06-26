remainder_premise = 47
dividend_premise = 288
remainder_hypothesis = 47
dividend_hypothesis = 588

# the hypothesis talks about the remainder of a division by a number, referenced also in the premise
if remainder_hypothesis != remainder_premise:
    # check if the remainder in the hypothesis contradicts the remainder reported in the premise
    label = "contradiction"
elif dividend_hypothesis != dividend_premise:
    # check if the dividend in the hypothesis contradicts the dividend reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
