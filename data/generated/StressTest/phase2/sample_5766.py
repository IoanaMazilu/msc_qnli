# Premise: If Dana gives her parents 5% of that amount back each month, how much will she still owe her parents after four years of college?
# Hypothesis: If Dana gives her parents more than 4% of that amount back each month, how much will she still owe her parents after four years of college?
# Golden Label: entailment

percentage_given_back_premise = 5
percentage_given_back_hypothesis = 4

# the hypothesis refers to the percentage Dana gives back each month
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact percentage Dana gives back
    # any percentage less than 'percentage_given_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

