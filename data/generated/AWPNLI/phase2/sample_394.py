# Premise: Joan has 8.0 orange balloons and her friend gives her 2.0 more.
# Hypothesis: Joan has 10.0 orange balloons now.
# Golden Label: entailment

initial_orange_balloons_premise = 8.0
received_orange_balloons_premise = 2.0
total_orange_balloons_hypothesis = 10.0

# the hypothesis refers to the number of orange balloons, which are also mentioned in the premise
# compute the total number of orange balloons in the premise
total_orange_balloons_premise = initial_orange_balloons_premise + received_orange_balloons_premise
if total_orange_balloons_hypothesis != total_orange_balloons_premise:
    # check if the number of orange balloons in the hypothesis contradicts the number of orange balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

