susan_weight_premise = 10 + anna_weight_premise
anna_weight_premise = 110 - susan_weight_premise

susan_weight_hypothesis = 40 + anna_weight_hypothesis
anna_weight_hypothesis = 110 - susan_weight_hypothesis

# Check if the hypothesis value contradicts the estimate of Susan's weight in the premise
if susan_weight_hypothesis < susan_weight_premise:
    label = "contradiction"
elif anna_weight_hypothesis!= anna_weight_premise:
    # Check if the number of Anna's weight in the hypothesis contradicts the number of Anna's weight reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
