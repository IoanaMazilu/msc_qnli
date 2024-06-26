# define variables for premise and hypothesis
joe_avg_premise = 45
num_tests_premise = 4

# define variables for hypothesis
joe_avg_hypothesis = 45
num_tests_hypothesis = float(3) + 1  # more than 3 equally weighted tests

# calculate the arithmetic mean for the premise and hypothesis
joe_avg_premise_mean = sum(num_tests_premise * [45]) / num_tests_premise
joe_avg_hypothesis_mean = sum(num_tests_hypothesis * [45]) / num_tests_hypothesis

# compare the two means
if joe_avg_premise_mean == joe_avg_hypothesis_mean:
    # if the two means are the same, the hypothesis is entailed by the premise
    label = "entailment"
elif joe_avg_premise_mean > joe_avg_hypothesis_mean:
    # if the premise mean is greater than the hypothesis mean, the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the premise mean is less than or equal to the hypothesis mean, the hypothesis is neutral with respect to the premise
    label = "neutral"

print(label)
