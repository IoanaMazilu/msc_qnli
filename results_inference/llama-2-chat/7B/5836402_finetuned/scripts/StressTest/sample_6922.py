earning_premise = 810
earning_hypothesis = 210

# the hypothesis refers to the earning of Michael, which is also mentioned in the premise
if earning_hypothesis <= earning_premise:
    # check if the earning in the hypothesis contradicts the estimate of 'earning_premise'
    label = "contradiction"
elif earning_hypothesis > earning_premise:
    # if the earning in the hypothesis is greater than the estimate in the premise, it is entailed
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
