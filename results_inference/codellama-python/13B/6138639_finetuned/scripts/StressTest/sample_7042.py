susan_weight_premise = 40
susan_weight_hypothesis = 10
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis talks about the weight of Susan and Anna, referenced also in the premise
if total_weight_hypothesis!= total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
elif susan_weight_hypothesis >= susan_weight_premise:
    # check if the weight difference of Susan in the hypothesis contradicts the estimate of less than'susan_weight_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight difference of Susan
    # any weight difference of Susan less than'susan_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
