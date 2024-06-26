women_premise = 2
men_premise = 2
women_hypothesis = 2
men_hypothesis = 2

# the hypothesis mentions the victims as two women and two men, which is also mentioned in the premise
if women_hypothesis!= women_premise:
    # check if the number of women from the hypothesis contradicts the number of women in the premise
    label = "contradiction"
elif men_hypothesis!= men_premise:
    # check if the number of men from the hypothesis contradicts the number of men in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
