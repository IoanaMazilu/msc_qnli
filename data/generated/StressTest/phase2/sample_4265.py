# Premise: In 3 years John will be twice as old as Frank.
# Hypothesis: In more than 3 years John will be twice as old as Frank.
# Golden Label: contradiction

years_premise = 3
years_hypothesis = 3

# the hypothesis talks about the number of years in the future when John will be twice as old as Frank
if years_hypothesis < years_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # in the premise, John will be twice as old as Frank exactly in 3 years
    # if the hypothesis refers to a period longer than 3 years, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

