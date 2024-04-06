# Premise: The sale was made to pay Yukos'US $27.5 billion tax bill, Yuganskneftegaz was originally sold for US $9.4 billion to a little known company Baikalfinansgroup which was later bought by the Russian state-owned oil company Rosneft.
# Hypothesis: Yuganskneftegaz cost US $27.5 billion.
# Golden Label: neutral

tax_bill_premise = 27.5e9
yuganskneftegaz_cost_hypothesis = 27.5e9
yuganskneftegaz_cost_premise = 9.4e9

# the hypothesis talks about the cost of Yuganskneftegaz, which is also mentioned in the premise
if yuganskneftegaz_cost_hypothesis != yuganskneftegaz_cost_premise:
    # check if the cost of Yuganskneftegaz in the hypothesis contradicts the cost of Yuganskneftegaz from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

