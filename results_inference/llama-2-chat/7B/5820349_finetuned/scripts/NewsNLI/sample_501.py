cartons_recalled_premise = 2498
deaths_premise = 13
deaths_hypothesis = 13

# the hypothesis mentions the number of cartons recalled and the number of deaths related to tainted cantaloupes, which are also mentioned in the premise
if cartons_recalled_premise!= deaths_hypothesis:
    # check if the number of cartons recalled in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
