# Premise: If Dana gives her parents less than 6% of that amount back each month, how much will she still owe her parents after four years of college?
# Hypothesis: If Dana gives her parents 4% of that amount back each month, how much will she still owe her parents after four years of college?
# Golden Label: neutral

percentage_premise = 6
percentage_hypothesis = 4

# the hypothesis refers to the percentage of the amount Dana gives back to her parents, also mentioned in the premise
if percentage_hypothesis >= percentage_premise:
    # check if the percentage in the hypothesis contradicts the premise, which mentions 'less than 6%'
    label = "contradiction"
elif percentage_hypothesis < percentage_premise:
    # if the percentage in the hypothesis is less than the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

