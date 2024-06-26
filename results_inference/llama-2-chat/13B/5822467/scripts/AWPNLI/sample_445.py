manufacturer_total_premise = 14797.0
women_premise = 4969.0
men_hypothesis = 9832.0

# compute the total number of bathing suits for men in the premise
men_premise = women_premise + men_hypothesis

if men_hypothesis > manufacturer_total_premise:
    # check if the number of bathing suits for men in the hypothesis contradicts the total supply
    label = "contradiction"
elif men_premise!= men_hypothesis:
    # check if the number of bathing suits for men in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
