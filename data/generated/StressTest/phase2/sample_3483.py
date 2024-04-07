# Premise: After working for 6 days, David was joined by Moore.
# Hypothesis: After working for less than 8 days, David was joined by Moore.
# Golden Label: entailment

working_days_premise = 6
working_days_hypothesis = 8

# the hypothesis refers to the number of days David worked alone, which is also mentioned in the premise
if working_days_premise >= working_days_hypothesis:
    # check if the number of 'working_days_premise' contradicts the hypothesis statement of less than 'working_days_hypothesis'
    label = "contradiction"
else:
    # if the number of 'working_days_premise' is less than 'working_days_hypothesis', it can be explicitly entailed from the hypothesis
    label = "entailment"

print(label)

