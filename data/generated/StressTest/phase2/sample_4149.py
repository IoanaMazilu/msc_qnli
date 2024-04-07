# Premise: Jane earned enough money by selling seashells at 25 cents each to buy several used paperback books at 55 cents each.
# Hypothesis: Jane earned enough money by selling seashells at less than 45 cents each to buy several used paperback books at 55 cents each.
# Golden Label: entailment

seashell_price_premise = 25
seashell_price_hypothesis = 45
book_price_premise = 55
book_price_hypothesis = 55

# the hypothesis refers to the prices of the seashells and books mentioned in the premise
if seashell_price_hypothesis < seashell_price_premise:
    # check if the hypothesis value contradicts the seashell price in the premise
    label = "contradiction"
elif book_price_hypothesis != book_price_premise:
    # check if the book price in the hypothesis contradicts the book price in the premise
    label = "contradiction"
else:
    # if the hypothesis prices do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

