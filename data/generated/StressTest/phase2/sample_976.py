# Premise: Jake, Paul and Hari together dig the well in more than 3 days.
# Hypothesis: Jake, Paul and Hari together dig the well in 8 days.
# Golden Label: neutral

dig_days_premise = 3
dig_days_hypothesis = 8

# the hypothesis speaks about the same well digging activity, referenced also in the premise
if dig_days_hypothesis <= dig_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'dig_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'dig_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

