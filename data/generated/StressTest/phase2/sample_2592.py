# Premise: Mary can do a piece of work in 26 days.
# Hypothesis: Mary can do a piece of work in less than 56 days.
# Golden Label: entailment

work_completion_time_premise = 26
work_completion_time_hypothesis = 56

# the hypothesis is referring to the time Mary takes to complete a piece of work, which is also mentioned in the premise
if work_completion_time_hypothesis <= work_completion_time_premise:
    # check if the hypothesis value contradicts the time reported in the premise
    label = "contradiction"
elif work_completion_time_hypothesis > work_completion_time_premise:
    # check if the hypothesis value is greater than the time reported in the premise
    # since the premise states an exact number of days, any number of days less than or equal to 'work_completion_time_premise' can be inferred
    label = "entailment"
else:
    # if the hypothesis value neither contradicts nor can be inferred from the premise, the relation is neutral
    label = "neutral"

print(label)

