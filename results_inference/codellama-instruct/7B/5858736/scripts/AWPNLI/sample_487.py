orange_balloons_premise = 9.0
blue_balloons_premise = 4.0
orange_balloons_found = 2.0
orange_balloons_hypothesis = 13.0

# the hypothesis refers to the number of orange balloons, which are also mentioned in the premise
# compute the total number of orange balloons in the premise
orange_balloons_premise_total = orange_balloons_premise + orange_balloons_found
if orange_balloons_hypothesis!= orange_balloons_premise_total:
    # check if the number of orange balloons in the hypothesis contradicts the number of orange balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
