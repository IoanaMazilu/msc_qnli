girls_premise = 542.0
boys_premise = 387.0
more_girls_hypothesis = 155.0

# compute the difference between the number of girls and boys
difference = girls_premise - boys_premise

# check if the difference is greater than the number of more girls in the hypothesis
if difference > more_girls_hypothesis:
    # if the difference is greater than the number of more girls, the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the difference is less than or equal to the number of more girls, the hypothesis is entailed by the premise
    label = "entailment"

print(label)
