# Premise: Kamal will complete work in 20 days.
# Hypothesis: Kamal will complete work in less than 40 days.
# Golden Label: entailment

work_days_premise = 20
work_days_hypothesis = 40

# the hypothesis talks about the number of days Kamal will work, which is also referenced in the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the number of 'work_days_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

