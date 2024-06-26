orange_balloons_premise = 9.0
blue_balloons_premise = 4.0
orange_balloons_found_premise = 2.0
orange_balloons_hypothesis = 13.0

# the hypothesis refers to the number of orange balloons, which is also mentioned in the premise
# compute the total number of orange balloons in the premise
total_orange_balloons_premise = orange_balloons_premise + orange_balloons_found_premise
if total_orange_balloons_premise!= orange_balloons_hypothesis:
    # check if the number of orange balloons in the hypothesis contradicts the number of orange balloons in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
