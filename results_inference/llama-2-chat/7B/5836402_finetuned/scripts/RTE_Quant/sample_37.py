production_costs_cut_premise = 25
production_costs_cut_hypothesis = 25

# the hypothesis talks about the percentage of production costs cut in Indonesia, which is also mentioned in the premise
if production_costs_cut_hypothesis!= production_costs_cut_premise:
    # check if the percentage of production costs cut in the hypothesis contradicts the percentage from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
