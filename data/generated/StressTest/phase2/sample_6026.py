# Premise: If Dana gives her parents 4% of that amount back each month, how much will she still owe her parents after four years of college?
# Hypothesis: If Dana gives her parents less than 4% of that amount back each month, how much will she still owe her parents after four years of college?
# Golden Label: contradiction

# Variables for the percentage of the amount Dana gives back each month
percentage_given_back_premise = 4
percentage_given_back_hypothesis = 4

# The hypothesis refers to the percentage of the amount Dana gives back each month, mentioned in the premise
if percentage_given_back_hypothesis < percentage_given_back_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif percentage_given_back_hypothesis > percentage_given_back_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentages in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)

