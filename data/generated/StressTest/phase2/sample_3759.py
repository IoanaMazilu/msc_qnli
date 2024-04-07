# Premise: Mary can do a piece of work in 12 days.
# Hypothesis: Mary can do a piece of work in less than 72 days.
# Golden Label: entailment

work_days_premise = 12
work_days_hypothesis = 72

# the hypothesis refers to the number of days Mary needs to complete a piece of work, also mentioned in the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
elif work_days_hypothesis == work_days_premise:
    # check if the number of days in the hypothesis is the same as the number of days in the premise
    label = "entailment"
else:
    # if the number of days in the hypothesis is more than the number of days in the premise, but still less than 'work_days_hypothesis', it's neutral
    label = "neutral"

print(label)

