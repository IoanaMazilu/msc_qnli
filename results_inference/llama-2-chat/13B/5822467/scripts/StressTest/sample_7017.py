seniors_premise = 300
seniors_hypothesis = 800
cars_premise = 40

# the hypothesis talks about the number of seniors and the percentage of them with cars, referenced also in the premise
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of more than'seniors_premise'
    label = "contradiction"
elif cars_premise!= cars_hypothesis:
    # check if the number of seniors with cars in the hypothesis contradicts the number of seniors with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)