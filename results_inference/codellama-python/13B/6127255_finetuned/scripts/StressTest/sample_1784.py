# The premise and hypothesis both refer to the ratio of their ages in the future
# The premise states that the ratio will be 5/3, the hypothesis states the ratio will be more than 5/3

ratio_premise = 5/3
ratio_hypothesis = 5/3

# The hypothesis is contradicting the premise because it is stating the ratio will be more than 5/3
if ratio_hypothesis <= ratio_premise:
    label = "contradiction"
else:
    # The premise does not provide any information about the ratio being less than 5/3
    # Therefore, the relation is neutral
    label = "neutral"

print(label)
