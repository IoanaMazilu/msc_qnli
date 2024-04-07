# Premise: Ram and Shyam can do together a piece of work in 20 days.
# Hypothesis: Ram and Shyam can do together a piece of work in more than 10 days.
# Golden Label: entailment

work_days_premise = 20
work_days_hypothesis = 10

# the hypothesis refers to the time it takes for Ram and Shyam to complete a piece of work mentioned in the premise
if work_days_premise < work_days_hypothesis:
    # check if the 'work_days_premise' contradicts the estimate of more than 'work_days_hypothesis'
    label = "contradiction"
elif work_days_premise == work_days_hypothesis:
    # the premise gives an exact number of days, any number less than 'work_days_premise' is a contradiction
    label = "contradiction"
else:
    # if the 'work_days_premise' does not contradict the 'work_days_hypothesis', we can infer entailment
    label = "entailment"

print(label)

