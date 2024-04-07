# Premise: Suraj has a certain average of runs for 8 innings.
# Hypothesis: Suraj has a certain average of runs for more than 5 innings.
# Golden Label: entailment

innings_premise = 8
innings_hypothesis = 5

# the hypothesis talks about the number of innings, referenced also in the premise
if innings_premise <= innings_hypothesis:
    # check if the premise value contradicts the estimate of more than 'innings_hypothesis'
    label = "contradiction"
elif innings_premise > innings_hypothesis:
    # any number of innings greater than 'innings_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "entailment"

print(label)

