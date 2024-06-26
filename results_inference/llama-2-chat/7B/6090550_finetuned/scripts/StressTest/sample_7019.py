seniors_premise = 300
seniors_hypothesis = 400
car_percentage_premise = 40
car_percentage_hypothesis = 40

# the hypothesis talks about the number of seniors and the percentage of them having cars, both referenced in the premise
if seniors_hypothesis!= seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the number of seniors in the premise
    label = "contradiction"
elif car_percentage_hypothesis!= car_percentage_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
