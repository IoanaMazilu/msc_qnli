# Premise: In 5 years John will be twice as old as Frank.
# Hypothesis: In 2 years John will be twice as old as Frank.
# Golden Label: contradiction

years_premise = 5
years_hypothesis = 2

# the hypothesis talks about the number of years in the future when John will be twice as old as Frank
if years_hypothesis == years_premise:
    # if the hypothesis' number of years matches the premise's, then it's an entailment
    label = "entailment"
else:
    # if the hypothesis' number of years does not match the premise's, then it's a contradiction
    label = "contradiction"

print(label)

