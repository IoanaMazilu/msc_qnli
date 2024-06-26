men_suits_premise = 14797.0
women_suits_premise = 4969.0
total_suits_hypothesis = 19766.0

# the hypothesis refers to the total number of bathing suits, which are also mentioned in the premise
# compute the total number of bathing suits from the premise
total_suits_premise = men_suits_premise + women_suits_premise
if total_suits_hypothesis!= total_suits_premise:
    # check if the total number of suits in the hypothesis contradicts the total number of suits from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
