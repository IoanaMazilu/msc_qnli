# Premise: less than 6 years ago Kate was 5 times as old as her Son.
# Hypothesis: 5 years ago Kate was 5 times as old as her Son.
# Golden Label: neutral

years_premise = 6
years_hypothesis = 5

# the hypothesis refers to the time frame mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the time frame in the hypothesis contradicts the premise 'less than years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time frame
    # any time frame less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

