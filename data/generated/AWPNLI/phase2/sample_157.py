# Premise: The clown blew up 47.0 balloons and then he blew up 13.0 more balloons.
# Hypothesis: Clown has 63.0 balloons now.
# Golden Label: contradiction

initial_balloons_premise = 47.0
additional_balloons_premise = 13.0
total_balloons_hypothesis = 63.0

# the hypothesis refers to the total number of balloons, which is also mentioned in the premise
# compute the total number of balloons in the premise
total_balloons_premise = initial_balloons_premise + additional_balloons_premise
if total_balloons_hypothesis != total_balloons_premise:
    # check if the total number of balloons in the hypothesis contradicts the total number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)

