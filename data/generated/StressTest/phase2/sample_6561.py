# Premise: If Jerry wants to raise his average by 2 points, what score must he earn on the fourth test?
# Hypothesis: If Jerry wants to raise his average by less than 6 points, what score must he earn on the fourth test?
# Golden Label: entailment

average_raise_premise = 2
average_raise_hypothesis = 6

# the hypothesis refers to the same situation as the premise, but with a different value for the average raise
if average_raise_premise > average_raise_hypothesis:
    # check if the 'average_raise_premise' contradicts the hypothesis's estimate of less than 'average_raise_hypothesis'
    label = "contradiction"
elif average_raise_premise == average_raise_hypothesis:
    # check if the 'average_raise_premise' exactly equals the 'average_raise_hypothesis'
    label = "contradiction"
else:
    # if the 'average_raise_premise' does not contradict the 'average_raise_hypothesis', we can infer entailment
    label = "entailment"

print(label)

