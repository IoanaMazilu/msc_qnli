# Premise: Jane earned enough money by selling seashells at 25 cents each to buy several used paperback books at 55 cents each.
# Hypothesis: Jane earned enough money by selling seashells at less than 25 cents each to buy several used paperback books at 55 cents each.
# Golden Label: contradiction

seashell_price_premise = 25
seashell_price_hypothesis = 25
book_price_premise = 55
book_price_hypothesis = 55

# hypothesis refers to the price of selling seashells and buying books
if seashell_price_hypothesis >= seashell_price_premise:
    # check if the hypothesis value contradicts the premise value for seashell price
    label = "contradiction"
elif book_price_hypothesis != book_price_premise:
    # check if the hypothesis value contradicts the premise value for book price
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

