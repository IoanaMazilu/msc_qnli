# Premise: '' There were two attempts on his life, one at his country home outside Moscow in a gated community.
# Hypothesis: He survived two attempts on his life, including a car bomb.
# Golden Label: neutral

attempts_premise = 2
attempts_hypothesis = 2

# the hypothesis mentions the number of attempts on his life, which is also referenced in the premise
# however, the hypothesis refers to the method of one attempt (a car bomb), which cannot be entailed from the premise
label = "neutral"

print(label)

