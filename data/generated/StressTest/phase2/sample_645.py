# Premise: On every Adidas shoe the restaurant makes a profit of $10 while on every Puma shoe it makes a profit of $8.
# Hypothesis: On every Adidas shoe the restaurant makes a profit of $less than 30 while on every Puma shoe it makes a profit of $8.
# Golden Label: entailment

adidas_profit_premise = 10
adidas_profit_hypothesis = 30
puma_profit_premise = 8
puma_profit_hypothesis = 8

# the hypothesis refers to the profit on Adidas and Puma shoes mentioned in the premise
if adidas_profit_premise >= adidas_profit_hypothesis:
    # check if the estimate of 'adidas_profit_hypothesis' contradicts the profit on Adidas shoes in the premise
    label = "contradiction"
elif puma_profit_hypothesis != puma_profit_premise:
    # check if the profit on Puma shoes in the hypothesis contradicts the profit on Puma shoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

