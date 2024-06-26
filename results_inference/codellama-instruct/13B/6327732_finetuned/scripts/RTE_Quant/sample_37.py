tin_industry_premise = "Indonesia's tin industry"
tin_mine_premise = "Tambang Timah"
production_costs_premise = 25
production_costs_hypothesis = 25

# the hypothesis talks about the production costs of the tin industry, which is also mentioned in the premise
if production_costs_hypothesis!= production_costs_premise:
    # check if the production costs in the hypothesis contradicts the production costs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
