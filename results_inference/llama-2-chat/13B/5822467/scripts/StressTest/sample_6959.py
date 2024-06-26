venkat_toys_premise = 375 * 20
venkat_toys_hypothesis = 675 * 20

# the hypothesis refers to the rate at which Venkat purchased the toys, which is also mentioned in the premise
if venkat_toys_hypothesis > venkat_toys_premise:
    # check if the hypothesis rate contradicts the rate reported in the premise
    label = "contradiction"
elif venkat_toys_hypothesis == venkat_toys_premise:
    # if the hypothesis rate is the same as the premise rate, there is no contradiction and no entailment
    label = "neutral"
else:
    # if the hypothesis rate is higher than the premise rate, it entails that Venkat purchased more toys
    label = "entailment"

print(label)
