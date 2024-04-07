# Premise: Suraj has a certain average of runs for more than 5 innings.
# Hypothesis: Suraj has a certain average of runs for 8 innings.
# Golden Label: neutral

innings_premise = 5
innings_hypothesis = 8

# the hypothesis talks about the number of innings Suraj played, which is also referenced in the premise
if innings_hypothesis <= innings_premise:
    # check if the hypothesis value contradicts the estimate of more than 'innings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of innings
    # any number of innings greater than 'innings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

