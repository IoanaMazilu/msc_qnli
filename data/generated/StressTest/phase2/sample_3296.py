# Premise: Jaime earned enough money by selling seashells at 20 cents each to buy several used paperback books at 55 cents each.
# Hypothesis: Jaime earned enough money by selling seashells at 50 cents each to buy several used paperback books at 55 cents each.
# Golden Label: contradiction

seashell_price_premise = 20
seashell_price_hypothesis = 50
book_price_premise = 55
book_price_hypothesis = 55

# the hypothesis talks about the price of seashells Jaime sold and price of used paperback books he bought, also referenced in the premise
if seashell_price_hypothesis < seashell_price_premise:
    # check if the price of seashells in the hypothesis contradicts the price in the premise
    label = "contradiction"
elif book_price_hypothesis != book_price_premise:
    # check if the price of used paperback books in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

