# Premise: If Jerry wants to raise his average by less than 8 points, what score must he earn on the fourth test?
# Hypothesis: If Jerry wants to raise his average by 2 points, what score must he earn on the fourth test?
# Golden Label: neutral

average_increase_premise = 8
average_increase_hypothesis = 2

# the hypothesis refers to the condition of Jerry wanting to raise his average score mentioned in the premise
if average_increase_hypothesis >= average_increase_premise:
    # check if the 'average_increase_hypothesis' contradicts the premise of the average increase being less than 'average_increase_premise'
    label = "contradiction"
else:
    # the premise gives an upper limit for the average increase
    # any target average increase less than 'average_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

