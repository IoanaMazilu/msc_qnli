# Premise: They both work together for 5 days and then Sushil goes away.
# Hypothesis: They both work together for less than 5 days and then Sushil goes away.
# Golden Label: contradiction

work_days_premise = 5
work_days_hypothesis = 5

# the hypothesis refers to the number of days they work together mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

