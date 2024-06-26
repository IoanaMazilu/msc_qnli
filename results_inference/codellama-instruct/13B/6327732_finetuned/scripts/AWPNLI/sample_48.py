supply_men_premise = 14797.0
supply_women_premise = 4969.0
total_supply_premise = supply_men_premise + supply_women_premise

supply_overall_hypothesis = 19766.0

if supply_overall_hypothesis!= total_supply_premise:
    # check if the number of bathing suits in the hypothesis contradicts the total number of bathing suits from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
