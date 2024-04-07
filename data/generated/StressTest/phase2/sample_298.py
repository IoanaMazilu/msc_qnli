# Premise: In more than 1 years John will be twice as old as Frank.
# Hypothesis: In 5 years John will be twice as old as Frank.
# Golden Label: neutral

years_john_premise = 1
years_john_hypothesis = 5

# the hypothesis talks about the future age of John and Frank, referenced also in the premise
if years_john_hypothesis <= years_john_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_john_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_john_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

