percentage_premise = 6/10
percentage_hypothesis = 6/10

# the hypothesis mentions the percentage of Americans believing that Boehner should lose his job, which is also referenced in the premise
if percentage_hypothesis > percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif percentage_hypothesis < percentage_premise:
    # check if the percentage from the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
