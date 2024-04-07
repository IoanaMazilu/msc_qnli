# Premise: Paul can dig the same well in less than 74 days.
# Hypothesis: Paul can dig the same well in 24 days.
# Golden Label: neutral

digging_days_premise = 74
digging_days_hypothesis = 24

# the hypothesis talks about the number of days Paul can dig a well, also referenced in the premise
if digging_days_hypothesis > digging_days_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'digging_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'digging_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

