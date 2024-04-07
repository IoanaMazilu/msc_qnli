# Premise: Jaime earned enough money by selling seashells at 35 cents each to buy several used paperback books at 55 cents each.
# Hypothesis: Jaime earned enough money by selling seashells at less than 35 cents each to buy several used paperback books at 55 cents each.
# Golden Label: contradiction

seashells_price_premise = 35
seashells_price_hypothesis = 35
books_price_premise = 55
books_price_hypothesis = 55

# the hypothesis refers to the price of sold seashells and the price of bought books mentioned in the premise
if seashells_price_hypothesis >= seashells_price_premise:
    # check if the estimate of 'seashells_price_hypothesis' contradicts the price of seashells in the premise
    label = "contradiction"
elif books_price_hypothesis != books_price_premise:
    # check if the price of the books in the hypothesis contradicts the price of the books reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

