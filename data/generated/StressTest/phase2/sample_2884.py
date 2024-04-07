# Premise: If Jerry wants to raise his average by more than 1 points, what score must he earn on the fourth test?
# Hypothesis: If Jerry wants to raise his average by 2 points, what score must he earn on the fourth test?
# Golden Label: neutral

average_increase_premise = 1
average_increase_hypothesis = 2

# the hypothesis talks about the points Jerry needs to raise his average by, referenced in the premise
if average_increase_hypothesis <= average_increase_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_increase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the points Jerry needs to raise his average by
    # any number of points greater than 'average_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

