# Premise: Cindy's mother gives her $30 to spend.
# Hypothesis: Cindy's mother gives her $40 to spend.
# Golden Label: contradiction

money_given_premise = 30
money_given_hypothesis = 40

# the hypothesis talks about the amount of money Cindy's mother gives her, referenced also in the premise
if money_given_hypothesis != money_given_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money given in the premise
    label = "contradiction"
else:
    # if the amount of money given in the hypothesis does not contradict the amount of money given in the premise, we can infer entailment
    label = "entailment"

print(label)

