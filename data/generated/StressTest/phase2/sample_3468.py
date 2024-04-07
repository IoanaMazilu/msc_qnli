# Premise: Sakshi can do a piece of work in 20 days.
# Hypothesis: Sakshi can do a piece of work in less than 30 days.
# Golden Label: entailment

work_days_premise = 20
work_days_hypothesis = 30

# the hypothesis refers to the number of days Sakshi needs for a piece of work, also mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif work_days_hypothesis > work_days_premise:
    # if the number of days in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"
else:
    # if neither contradiction nor entailment can be inferred, we label as neutral
    label = "neutral"

print(label)

