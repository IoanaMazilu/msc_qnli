# Premise: In 5 years John will be twice as old as Frank.
# Hypothesis: In less than 8 years John will be twice as old as Frank.
# Golden Label: entailment

years_premise = 5
years_hypothesis = 8

# the hypothesis refers to the condition mentioned in the premise but in a different timeframe
if years_hypothesis <= years_premise:
    # check if the timeframe in the hypothesis contradicts the timeframe in the premise
    label = "contradiction"
else:
    # the premise does not provide explicit information about John's and Frank's age in more than 5 years 
    # any condition in 'years_hypothesis' years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

