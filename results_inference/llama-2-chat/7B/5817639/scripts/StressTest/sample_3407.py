jill_wage_premise = 4.0
jill_wage_hypothesis = 4.0
tip_rate_premise = 0.15
tip_rate_hypothesis = 0.65

# the hypothesis refers to the tip rate, which is not mentioned in the premise
if jill_wage_hypothesis <= jill_wage_premise:
    # check if the hypothesis value contradicts the estimate of 'jill_wage_premise'
    label = "contradiction"
elif tip_rate_hypothesis!= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
