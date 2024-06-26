men_premise = 2
women_premise = 2
men_hypothesis = 2
women_hypothesis = 2

# the hypothesis mentions the number of men and women killed, which are also mentioned in the premise
if men_hypothesis!= men_premise:
    # check if the number of men in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
elif women_hypothesis!= women_premise:
    # check if the number of women from the hypothesis contradicts the number of women in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
