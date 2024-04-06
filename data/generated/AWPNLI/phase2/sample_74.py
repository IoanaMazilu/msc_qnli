# Premise: Jason has 7.0 violet balloons and 4.0 red balloons and he lost 3.0 of the violet balloons.
# Hypothesis: Jason has 4.0 violet balloons now.
# Golden Label: entailment

violet_balloons_premise = 7.0
lost_violet_balloons_premise = 3.0
violet_balloons_hypothesis = 4.0

# the hypothesis refers to the number of violet balloons, which is also mentioned in the premise
# compute the remaining number of violet balloons in the premise
remaining_violet_balloons_premise = violet_balloons_premise - lost_violet_balloons_premise
if violet_balloons_hypothesis != remaining_violet_balloons_premise:
    # check if the number of violet balloons in the hypothesis contradicts the number of violet balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

