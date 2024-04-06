# Premise: Sally has 9.0 orange balloons and 4.0 blue balloons and she found 2.0 more of the orange balloons.
# Hypothesis: Sally has 13.0 orange balloons now.
# Golden Label: contradiction

orange_balloons_premise = 9.0
found_orange_balloons_premise = 2.0
orange_balloons_hypothesis = 13.0

# the hypothesis refers to the number of orange balloons, which are also mentioned in the premise
# compute the total number of orange balloons in the premise
total_orange_balloons_premise = orange_balloons_premise + found_orange_balloons_premise
if orange_balloons_hypothesis != total_orange_balloons_premise:
    # check if the number of orange balloons in the hypothesis contradicts the number of orange balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)

