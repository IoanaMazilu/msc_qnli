# Premise: Jimmy's paper has less than 52, 24, 36, 48, and a blank space. What number should Jimmy B put in the blank space?
# Hypothesis: Jimmy's paper has 12, 24, 36, 48, and a blank space. What number should Jimmy B put in the blank space?
# Golden Label: neutral

numbers_premise = [52, 24, 36, 48]
numbers_hypothesis = [12, 24, 36, 48]

# the hypothesis refers to the numbers mentioned on Jimmy's paper in the premise
# we compare each corresponding pair of numbers between the premise and the hypothesis
for num_premise, num_hypothesis in zip(numbers_premise, numbers_hypothesis):
    if num_hypothesis >= num_premise:
        # check if the number in the hypothesis contradicts the estimate of less than the number in the premise
        label = "contradiction"
        break
else:
    # the premise gives only an estimate for the numbers
    # any set of numbers lower than those in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

