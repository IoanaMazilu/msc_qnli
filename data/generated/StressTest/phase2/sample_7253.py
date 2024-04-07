# Premise: Suraj has a certain average of runs for 8 innings.
# Hypothesis: Suraj has a certain average of runs for 4 innings.
# Golden Label: contradiction

innings_premise = 8
innings_hypothesis = 4

# the hypothesis talks about the number of innings, referenced also in the premise
if innings_hypothesis > innings_premise:
    # check if the hypothesis value contradicts the reported number of innings in the premise
    label = "contradiction"
elif innings_hypothesis == innings_premise:
    # check if the hypothesis value matches exactly the number of innings in the premise
    label = "entailment"
else:
    # the premise gives a certain number of innings
    # a smaller number of innings is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

