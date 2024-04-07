# Premise: Ram and Shyam can do together a piece of work in more than 10 days.
# Hypothesis: Ram and Shyam can do together a piece of work in 20 days.
# Golden Label: neutral

work_days_premise = 10
work_days_hypothesis = 20

# the hypothesis talks about the number of days Ram and Shyam can complete a piece of work, which is also referenced in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

