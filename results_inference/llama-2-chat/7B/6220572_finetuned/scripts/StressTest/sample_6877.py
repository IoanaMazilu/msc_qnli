total_ages_premise = 86
total_ages_hypothesis = 66

# the hypothesis refers to the total ages of three people mentioned in the premise
if total_ages_hypothesis <= total_ages_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_ages_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total ages
    # any total age less than 'total_ages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
