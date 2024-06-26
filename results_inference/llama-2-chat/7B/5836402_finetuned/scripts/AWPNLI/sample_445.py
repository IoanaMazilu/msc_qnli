total_suits_premise = 14797.0
women_suits_premise = 4969.0
men_suits_hypothesis = 9832.0

# the hypothesis refers to the number of bathing suits for men, which is also mentioned in the premise
# compute the total number of bathing suits for men in the premise
men_suits_premise = total_suits_premise - women_suits_premise
if men_suits_hypothesis!= men_suits_premise:
    # check if the number of bathing suits for men in the hypothesis contradicts the number of suits from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
