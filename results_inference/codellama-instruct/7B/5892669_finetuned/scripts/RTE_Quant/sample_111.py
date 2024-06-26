yukos_tax_premise = 27.5e9
yuganskneftegaz_sale_premise = 9.4e9
yuganskneftegaz_sale_hypothesis = 27.5e9

# the hypothesis talks about the sale value of Yuganskneftegaz, which is also mentioned in the premise
if yuganskneftegaz_sale_hypothesis!= yuganskneftegaz_sale_premise:
    # check if the sale value of Yuganskneftegaz in the hypothesis contradicts the sale value from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
