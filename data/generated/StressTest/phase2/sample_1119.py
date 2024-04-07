# Premise: Suraj has a certain average of runs for 12 innings.
# Hypothesis: Suraj has a certain average of runs for less than 62 innings.
# Golden Label: entailment

innings_premise = 12
innings_hypothesis = 62

# the hypothesis talks about the average of runs in a number of innings, referenced also in the premise
if innings_hypothesis <= innings_premise:
    # check if the hypothesis value contradicts the definite number of 'innings_premise'
    label = "contradiction"
else:
    # the premise gives only a certain number of innings
    # any number of innings less than 'innings_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

