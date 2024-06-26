shirt_count_premise = 1
jeans_count_premise = 1
sneakers_count_premise = 1

shirt_count_hypothesis = 0
jeans_count_hypothesis = 0
sneakers_count_hypothesis = 0

if shirt_count_hypothesis < shirt_count_premise:
    label = "contradiction"
elif jeans_count_hypothesis < jeans_count_premise:
    label = "contradiction"
elif sneakers_count_hypothesis < sneakers_count_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
