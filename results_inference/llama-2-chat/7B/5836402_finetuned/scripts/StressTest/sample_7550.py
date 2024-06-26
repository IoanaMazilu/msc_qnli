saving_amount_decrease_premise = 30
saving_amount_decrease_hypothesis = 20

# the hypothesis refers to the percentage of saving amount decreased, which is also mentioned in the premise
if saving_amount_decrease_hypothesis!= saving_amount_decrease_premise:
    # check if the percentage of saving amount decrease in the hypothesis contradicts the percentage of saving amount decrease reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
