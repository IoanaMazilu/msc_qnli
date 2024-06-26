efficiency_premise = 0.35
efficiency_hypothesis = 0.25
days_premise = ---
days_hypothesis = ---

# the hypothesis refers to the efficiency of Suresh and the number of days he can complete the work
if efficiency_hypothesis <= efficiency_premise:
    # check if the hypothesis value contradicts the estimate of 'efficiency_premise'
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
