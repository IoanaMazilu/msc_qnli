jim_cleans_premise = 6
jim_cleans_hypothesis = 1

# the hypothesis refers to the time taken by Jim to clean the entire house
if jim_cleans_hypothesis > jim_cleans_premise:
    # the hypothesis entails the premise, as the time taken is greater than the premise
    label = "entailment"
elif jim_cleans_hypothesis == jim_cleans_premise:
    # the hypothesis is neutral, as the time taken is the same as the premise
    label = "neutral"
else:
    # the hypothesis contradicts the premise, as the time taken is less than the premise
    label = "contradiction"

print(label)
