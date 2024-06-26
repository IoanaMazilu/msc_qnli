num_slaves_premise = 30000000
num_slaves_hypothesis = 30000000

# the hypothesis mentions the same number of slaves as the premise

# check if the values are the same
if num_slaves_hypothesis == num_slaves_premise:
    # if the values are the same, there is no contradiction or entailment
    label = "neutral"
else:
    # if the values are different, check for contradiction
    label = "contradiction"

print(label)
