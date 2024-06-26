pen_total_premise = 12
pen_total_hypothesis = 12
pen_price_premise = 42.00
pen_price_hypothesis = 42.00

# the hypothesis refers to the number of pens purchased and the price paid, mentioned in the premise
if pen_total_premise <= pen_total_hypothesis:
    # check if the estimate of 'pen_total_hypothesis' contradicts the number of pens purchased in the premise
    label = "contradiction"
elif pen_price_hypothesis!= pen_price_premise:
    # check if the price paid in the hypothesis contradicts the price paid in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
