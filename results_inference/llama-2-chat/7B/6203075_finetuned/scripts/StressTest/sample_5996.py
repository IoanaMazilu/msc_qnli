women_premise = 4
men_premise = 1
women_hypothesis = 1
men_hypothesis = 1

# the hypothesis refers to the number of women and men on the board of education
if women_premise!= women_hypothesis:
    # check if the number of women in the hypothesis contradicts the number of women in the premise
    label = "contradiction"
elif men_premise!= men_hypothesis:
    # check if the number of men in the hypothesis contradicts the number of men in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
