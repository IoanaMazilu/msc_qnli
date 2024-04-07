# Premise: Lexi needed to save for 30 days to afford a vacation at the job that paid her $125 per day.
# Hypothesis: Lexi needed to save for more than 30 days to afford a vacation at the job that paid her $125 per day.
# Golden Label: contradiction

save_days_premise = 30
save_days_hypothesis = 30
salary_per_day = 125

# the hypothesis refers to the number of days Lexi needed to save at her job, mentioned in the premise
if save_days_hypothesis > save_days_premise:
    # check if the estimate of 'save_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif save_days_hypothesis < save_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

