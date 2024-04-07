# Premise: Jaime earned enough money by selling seashells at 20 cents each to buy several used paperback books at 55 cents each.
# Hypothesis: Jaime earned enough money by selling seashells at less than 30 cents each to buy several used paperback books at 55 cents each.
# Golden Label: entailment

seashell_price_premise = 20
seashell_price_hypothesis = 30
book_price_premise = 55
book_price_hypothesis = 55

# the hypothesis talks about the price at which Jaime sold seashells and the price of the books he bought, both referenced in the premise
if seashell_price_hypothesis < seashell_price_premise:
    # check if the hypothesis value contradicts the price at which Jaime sold seashells in the premise
    label = "contradiction"
elif book_price_hypothesis != book_price_premise:
    # check if the price of books in the hypothesis contradicts the price of books reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

