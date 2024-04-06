# Premise: Jason has 7.0 violet balloons and 4.0 red balloons and he lost 3.0 of the violet balloons.
# Hypothesis: Jason has 3.0 violet balloons now.
# Golden Label: contradiction

violet_balloons_premise = 7.0
red_balloons_premise = 4.0
lost_violet_balloons_premise = 3.0
violet_balloons_hypothesis = 3.0

# The hypothesis refers to the number of violet balloons Jason has now, which is also mentioned in the premise
# Compute the current number of violet balloons in the premise
current_violet_balloons_premise = violet_balloons_premise - lost_violet_balloons_premise
if violet_balloons_hypothesis != current_violet_balloons_premise:
    # Check if the number of violet balloons in the hypothesis contradicts the number of violet balloons from the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

