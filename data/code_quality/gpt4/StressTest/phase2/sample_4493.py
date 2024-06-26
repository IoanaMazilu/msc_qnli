tanya_efficiency_premise = 25
tanya_efficiency_hypothesis = 15

# the hypothesis refers to Tanya's efficiency rate compared to Sakshi's, which is also mentioned in the premise
if tanya_efficiency_hypothesis > tanya_efficiency_premise:
    # check if the efficiency rate in the hypothesis contradicts the efficiency rate in the premise
    label = "contradiction"
elif tanya_efficiency_hypothesis < tanya_efficiency_premise:
    # check if the efficiency rate in the hypothesis is less than the efficiency rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
