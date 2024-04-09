susan_weight_premise = 10
anna_weight_premise = 10
total_weight_premise = 110

susan_weight_hypothesis = 40
anna_weight_hypothesis = 10
total_weight_hypothesis = 110

# compare the values of the hypothesis with the premise
if susan_weight_hypothesis <= susan_weight_premise:
    # check if the hypothesis value contradicts the estimate of'susan_weight_premise'
    label = "contradiction"
elif anna_weight_hypothesis!= anna_weight_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
