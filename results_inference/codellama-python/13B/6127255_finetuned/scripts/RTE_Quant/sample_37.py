tin_industry_profit_year_premise = 1992
tin_production_cost_cut_percentage_premise = 25
tin_production_cost_cut_percentage_hypothesis = 25

# the hypothesis talks about the production cost cut percentage in Indonesia, which is also mentioned in the premise
if tin_production_cost_cut_percentage_hypothesis!= tin_production_cost_cut_percentage_premise:
    # check if the production cost cut percentage in the hypothesis contradicts the production cost cut percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
