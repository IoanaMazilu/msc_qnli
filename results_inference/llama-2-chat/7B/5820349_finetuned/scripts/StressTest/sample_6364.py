watermelons_left_premise = 536
watermelons_left_hypothesis = 136

# the hypothesis talks about the number of watermelons left after Sally left, referenced also in the premise
if watermelons_left_hypothesis >= watermelons_left_premise:
    # check if the hypothesis value contradicts the estimate of less than 'watermelons_left_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of watermelons
    # any number of watermelons less than 'watermelons_left_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
