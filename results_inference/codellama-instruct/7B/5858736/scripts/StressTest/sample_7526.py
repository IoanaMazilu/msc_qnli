# define variables for the premise and hypothesis
num_passengers_premise = 4
num_passengers_hypothesis = 4

# extract the quantities as valid numbers
num_passengers_premise = int(num_passengers_premise)
num_passengers_hypothesis = int(num_passengers_hypothesis)

# perform calculations if necessary
num_combinations_premise = 6 * 5 * 4 * 3
num_combinations_hypothesis = 6 * 5 * 4 * 3 * 2

# compare the values and infer the label
if num_combinations_hypothesis > num_combinations_premise:
    label = "entailment"
elif num_combinations_hypothesis == num_combinations_premise:
    label = "neutral"
else:
    label = "contradiction"

print(label)
