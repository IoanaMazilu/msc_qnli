# Premise: Mary can do a piece of work in 11 days.
# Hypothesis: Mary can do a piece of work in less than 81 days.
# Golden Label: entailment

work_days_premise = 11
work_days_hypothesis = 81

# The hypothesis mentions the number of days Mary needs to finish a piece of work, which is also mentioned in the premise
if work_days_premise >= work_days_hypothesis:
    # Check if the number of days in the premise contradicts the estimate of less than 'work_days_hypothesis' days
    label = "contradiction"
else:
    # If the number of days in the premise is less than 'work_days_hypothesis', it doesn't contradict the hypothesis, so we can infer entailment
    label = "entailment"

print(label)

