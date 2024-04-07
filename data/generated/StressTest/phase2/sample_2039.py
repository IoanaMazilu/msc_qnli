# Premise: Donald has $900 in ten, twenty, fifty and one hundred dollar bills.
# Hypothesis: Donald has $400 in ten, twenty, fifty and one hundred dollar bills.
# Golden Label: contradiction

money_donald_premise = 900
money_donald_hypothesis = 400

# the hypothesis refers to the total amount of money that Donald has
if money_donald_premise != money_donald_hypothesis:
    # check if the total money in the hypothesis contradicts the total money reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

