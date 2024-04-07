# Premise: Suraj has a certain average of runs for more than 7 innings.
# Hypothesis: Suraj has a certain average of runs for 9 innings.
# Golden Label: neutral

innings_premise = 7
innings_hypothesis = 9

# the hypothesis talks about the number of innings Suraj has played, which is also mentioned in the premise
if innings_hypothesis <= innings_premise:
    # check if the number of innings in the hypothesis contradicts the information provided in the premise
    label = "contradiction"
else:
    # the premise gives only a minimum estimate for the number of innings
    # any number of innings greater than 'innings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

