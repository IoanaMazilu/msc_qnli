bathing_suits_total_premise = 14797.0
bathing_suits_women_premise = 4969.0
bathing_suits_men_hypothesis = 9832.0

# the hypothesis refers to the number of bathing suits for men, which are also mentioned in the premise
# compute the total number of bathing suits for men in the premise
bathing_suits_men_premise = bathing_suits_total_premise - bathing_suits_women_premise
if bathing_suits_men_hypothesis!= bathing_suits_men_premise:
    # check if the number of bathing suits for men in the hypothesis contradicts the number of bathing suits for men in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
