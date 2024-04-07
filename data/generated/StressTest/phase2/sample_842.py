# Premise: Jacob's age 18 years hence will be thrice his age four years ago.
# Hypothesis: Jacob's age less than 18 years hence will be thrice his age four years ago.
# Golden Label: contradiction

years_hence_premise = 18
years_hence_hypothesis = 18
years_ago = 4

# the hypothesis talks about Jacob's age in future and past years just as the premise
if years_hence_hypothesis >= years_hence_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the value of 'years_hence_hypothesis' is less than 'years_hence_premise', it means that the hypothesis does not contradict the premise
    # but the premise does not provide enough information to entail the hypothesis
    label = "neutral"

print(label)

