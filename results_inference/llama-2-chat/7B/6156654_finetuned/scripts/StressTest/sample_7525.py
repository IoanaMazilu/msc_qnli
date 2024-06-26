# The premise gives the number of combinations of more than 2 passengers that can be formed from John's 6 friends
combinations_premise = 6 * (6 - 2)

# The hypothesis gives the number of combinations of 4 passengers that can be formed from John's 6 friends
combinations_hypothesis = 6 * 4

# The hypothesis talks about the number of combinations of passengers, which is also mentioned in the premise
if combinations_hypothesis == combinations_premise:
    # If the number of combinations in the hypothesis matches the number of combinations in the premise, we can infer entailment
    label = "entailment"
else:
    # If the number of combinations in the hypothesis does not match the number of combinations in the premise, we can infer contradiction
    label = "contradiction"

print(label)
