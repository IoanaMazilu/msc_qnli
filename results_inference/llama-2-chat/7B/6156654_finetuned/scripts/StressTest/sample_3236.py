seniors_premise = 300
seniors_hypothesis = 300
cars_premise = 50
cars_hypothesis = 50

# the hypothesis refers to the number of seniors and cars at Morse High School, which are also mentioned in the premise
if seniors_premise!= seniors_hypothesis:
    # check if the number of seniors in the hypothesis contradicts the number of seniors in the premise
    label = "contradiction"
elif cars_premise!= cars_hypothesis:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
