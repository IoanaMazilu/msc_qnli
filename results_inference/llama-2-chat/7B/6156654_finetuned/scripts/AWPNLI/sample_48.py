men_suits = 14797.0
women_suits = 4969.0
total_suits = men_suits + women_suits

# the hypothesis refers to the total number of bathing suits, which is also mentioned in the premise
if total_suits!= 19766.0:
    # check if the total number of suits in the hypothesis contradicts the total number of suits in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values match, we can infer entailment
    label = "entailment"

print(label)
