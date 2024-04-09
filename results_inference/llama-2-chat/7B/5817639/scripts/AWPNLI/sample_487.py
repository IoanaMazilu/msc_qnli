orange_balloons_premise = 9.0
blue_balloons_premise = 4.0
found_orange_balloons = 2.0
orange_balloons_hypothesis = 13.0

# compare the number of orange balloons in the hypothesis with the number found in the premise
if orange_balloons_hypothesis >= orange_balloons_premise:
    # check if the number of orange balloons in the hypothesis contradicts the number found in the premise
    label = "contradiction"
elif orange_balloons_hypothesis - orange_balloons_premise!= 0:
    # check if the number of orange balloons in the hypothesis is greater than the number found in the premise, but not by more than 1
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
