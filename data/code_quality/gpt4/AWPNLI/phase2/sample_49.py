men_bathing_suits_premise = 14797.0
women_bathing_suits_premise = 4969.0
total_bathing_suits_hypothesis = 19770.0

# the hypothesis refers to the total number of bathing suits, which are also mentioned in the premise
# compute the total number of bathing suits in the premise
total_bathing_suits_premise = men_bathing_suits_premise + women_bathing_suits_premise
if total_bathing_suits_hypothesis != total_bathing_suits_premise:
    # check if the total number of bathing suits in the hypothesis contradicts the total number of bathing suits from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
