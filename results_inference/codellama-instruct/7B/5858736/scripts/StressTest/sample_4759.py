shirt_premise = 5
jeans_premise = 1
sneakers_premise = 1
shirt_hypothesis = 1
jeans_hypothesis = 1
sneakers_hypothesis = 1

if shirt_hypothesis > shirt_premise or jeans_hypothesis > jeans_premise or sneakers_hypothesis > sneakers_premise:
    label = "contradiction"
elif shirt_hypothesis < shirt_premise or jeans_hypothesis < jeans_premise or sneakers_hypothesis < sneakers_premise:
    label = "neutral"
else:
    label = "entailment"

print(label)
