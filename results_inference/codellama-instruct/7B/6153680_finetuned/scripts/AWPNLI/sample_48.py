men_bathing_suits = 14797.0
women_bathing_suits = 4969.0
overall_bathing_suits = men_bathing_suits + women_bathing_suits

# hypothesis refers to the total number of bathing suits available
if overall_bathing_suits!= 19766.0:
    # check if the hypothesis value contradicts the number of bathing suits available
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the number of bathing suits available, we can infer entailment
    label = "entailment"

print(label)
