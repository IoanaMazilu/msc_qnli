# Premise: A bathing suit manufacturer has a supply of 14797.0 bathing suits in total and it has 4969.0 bathing suits for women.
# Hypothesis: 9828.0 bathing suits are there for men.
# Golden Label: entailment

total_bathing_suits_premise = 14797.0
women_bathing_suits_premise = 4969.0
men_bathing_suits_hypothesis = 9828.0

# the hypothesis refers to the number of bathing suits for men, which is not directly mentioned in the premise
# compute the number of bathing suits for men in the premise
men_bathing_suits_premise = total_bathing_suits_premise - women_bathing_suits_premise
if men_bathing_suits_hypothesis != men_bathing_suits_premise:
    # check if the number of bathing suits for men in the hypothesis contradicts the number of bathing suits for men from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
