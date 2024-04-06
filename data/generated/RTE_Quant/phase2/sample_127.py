# Premise: GUS on Friday disposed of its remaining home shopping business and last non-UK retail operation with the% u20AC390m (£265m) sale of the Dutch home shopping company, Wehkamp, to Industri Kapital, a private equity firm.
# Hypothesis: Wehkamp cost% u20AC390m.
# Golden Label: entailment

sale_price_premise = 390e6
sale_price_hypothesis = 390e6

# the hypothesis talks about the sale price of Wehkamp which is also mentioned in the premise
if sale_price_hypothesis != sale_price_premise:
    # check if the sale price in the hypothesis contradicts the sale price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

