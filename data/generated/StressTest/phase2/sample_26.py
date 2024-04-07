# Premise: How many minutes does it take Dhoni to type 64 words if he types at the rate of 16 words per minute?
# Hypothesis: How many minutes does it take Dhoni to type 54 words if he types at the rate of 16 words per minute?
# Golden Label: contradiction

words_premise = 64
rate_premise = 16
time_premise = words_premise / rate_premise

words_hypothesis = 54
rate_hypothesis = 16
time_hypothesis = words_hypothesis / rate_hypothesis

# the hypothesis refers to the time it takes for Dhoni to type a certain number of words
# both hypothesis and premise use the same typing rate
if time_hypothesis > time_premise:
    # check if the time estimate in the hypothesis contradicts the time calculated using the premise values
    label = "contradiction"
elif words_hypothesis != words_premise:
    # check if the number of words in the hypothesis contradicts the number of words in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

