seniors_premise = 300
seniors_hypothesis = 400
percentage_with_cars_premise = 40
percentage_with_cars_hypothesis = 40

# the hypothesis refers to the number of seniors and the percentage of seniors with cars mentioned in the premise
if seniors_hypothesis!= seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the number of seniors reported in the premise
    label = "contradiction"
elif percentage_with_cars_hypothesis!= percentage_with_cars_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
