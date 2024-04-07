# Premise: Sakshi can do a piece of work in 20 days.
# Hypothesis: Sakshi can do a piece of work in more than 10 days.
# Golden Label: entailment

work_days_premise = 20
work_days_hypothesis = 10

# the hypothesis refers to the number of days Sakshi can do a piece of work, mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
