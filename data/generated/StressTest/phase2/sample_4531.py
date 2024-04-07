# Premise: Molly can do a task in less than 45 days while Sandy can do the task in 30 days.
# Hypothesis: Molly can do a task in 15 days while Sandy can do the task in 30 days.
# Golden Label: neutral

molly_days_premise = 45
molly_days_hypothesis = 15
sandy_days_premise = 30
sandy_days_hypothesis = 30

# the hypothesis talks about the number of days Molly and Sandy can complete a task
# these numbers are also mentioned in the premise

if molly_days_hypothesis >= molly_days_premise:
    # check if the number of days Molly needs to complete a task contradicts the premise
    label = "contradiction"
elif sandy_days_hypothesis != sandy_days_premise:
    # check if the number of days Sandy needs to complete a task contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Molly needs
    # any number of days less than 'molly_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

