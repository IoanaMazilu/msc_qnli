# Premise: Jaime earned enough money by selling seashells at 35 cents each to buy several used paperback books at 55 cents each.
# Hypothesis: Jaime earned enough money by selling seashells at more than 25 cents each to buy several used paperback books at 55 cents each.
# Golden Label: entailment

seashell_price_premise = 35
seashell_price_hypothesis = 25
book_price_premise = 55
book_price_hypothesis = 55

# the hypothesis speaks about the prices of seashells and books mentioned also in the premise
if seashell_price_premise <= seashell_price_hypothesis:
    # check if the price 'seashell_price_hypothesis' contradicts the price of seashells in the premise
    label = "contradiction"
elif book_price_hypothesis != book_price_premise:
    # check if the price of books in the hypothesis contradicts the price of books in the premise
    label = "contradiction"
else:
    # if the hypothesis prices do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

