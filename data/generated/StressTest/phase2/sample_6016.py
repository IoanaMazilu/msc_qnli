# Premise: Jane started baby-sitting when she was less than 40 years old.
# Hypothesis: Jane started baby-sitting when she was 20 years old.
# Golden Label: neutral

start_age_premise = 40
start_age_hypothesis = 20

# the hypothesis talks about the age Jane started babysitting, referenced also in the premise
if start_age_hypothesis >= start_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'start_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age Jane started babysitting
    # any age less than 'start_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

