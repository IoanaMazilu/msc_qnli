# Premise: Lexi needed to save for 30 days to afford a vacation at the job that paid her $125 per day.
# Hypothesis: Lexi needed to save for less than 80 days to afford a vacation at the job that paid her $125 per day.
# Golden Label: entailment

saving_days_premise = 30
saving_days_hypothesis = 80
pay_per_day = 125

# the hypothesis refers to the number of saving days needed by Lexi, mentioned also in the premise
if saving_days_premise >= saving_days_hypothesis:
    # check if the estimate of 'saving_days_hypothesis' contradicts the number of saving days in the premise
    label = "contradiction"
elif saving_days_premise < saving_days_hypothesis:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

