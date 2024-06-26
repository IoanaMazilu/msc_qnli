total_bathing_suits_premise = 14797
women_bathing_suits_premise = 4969
men_bathing_suits_hypothesis = 9832

# the hypothesis refers to the number of bathing suits for men, which is also referenced in the premise
# compute the number of bathing suits for men in the premise
men_bathing_suits_premise = total_bathing_suits_premise - women_bathing_suits_premise
if men_bathing_suits_hypothesis!= men_bathing_suits_premise:
    # check if the number of bathing suits for men in the hypothesis contradicts the number of bathing suits from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
