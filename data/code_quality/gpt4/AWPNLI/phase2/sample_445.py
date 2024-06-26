total_suits_premise = 14797.0
women_suits_premise = 4969.0
men_suits_hypothesis = 9832.0

# the hypothesis refers to the number of men's bathing suits, which can be estimated from the premise
# compute the number of men's bathing suits in the premise
men_suits_premise = total_suits_premise - women_suits_premise

if men_suits_hypothesis != men_suits_premise:
    # check if the number of men's bathing suits in the hypothesis contradicts the number of men's bathing suits from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
