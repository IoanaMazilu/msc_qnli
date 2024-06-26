men_premise = 4
men_hypothesis = 1

# the hypothesis refers to the number of men on the board of education, which is also mentioned in the premise
if men_hypothesis!= men_premise:
    # check if the number of men in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
