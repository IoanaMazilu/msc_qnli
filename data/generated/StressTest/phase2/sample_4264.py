# Premise: In less than 6 years John will be twice as old as Frank.
# Hypothesis: In 3 years John will be twice as old as Frank.
# Golden Label: neutral

john_age_multiplier_premise = 6
john_age_multiplier_hypothesis = 3

# the hypothesis talks about the number of years until John is twice as old as Frank, referenced in the premise
if john_age_multiplier_hypothesis >= john_age_multiplier_premise:
    # check if the hypothesis value contradicts the estimate of less than 'john_age_multiplier_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years less than 'john_age_multiplier_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

