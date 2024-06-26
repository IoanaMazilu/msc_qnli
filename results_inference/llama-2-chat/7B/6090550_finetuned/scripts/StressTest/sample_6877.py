y_premise = 86
age_hypothesis = 66

# the hypothesis talks about the total age of Amar, Akbar and Anthony, which is also mentioned in the premise
if age_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the estimate of less than 'y_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total age
    # any total age less than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
