# Premise: Jaime earned enough money by selling seashells at 30 cents each to buy several used paperback books at 55 cents each.
# Hypothesis: Jaime earned enough money by selling seashells at less than 30 cents each to buy several used paperback books at 55 cents each.
# Golden Label: contradiction

seashell_price_premise = 30
seashell_price_hypothesis = 30
book_price_premise = 55
book_price_hypothesis = 55

# the hypothesis refers to the price of seashells and books mentioned in the premise
if seashell_price_hypothesis >= seashell_price_premise:
    # check if the estimate of 'seashell_price_hypothesis' contradicts the price of seashells in the premise
    label = "contradiction"
elif book_price_hypothesis != book_price_premise:
    # check if the price of books in the hypothesis contradicts the price of books reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

