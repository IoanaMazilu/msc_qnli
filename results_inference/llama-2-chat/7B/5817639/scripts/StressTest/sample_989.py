seniors_premise = 300
seniors_hypothesis = 300
car_percentage_premise = 0.5
car_percentage_hypothesis = 0.5

# the hypothesis talks about the number of seniors and the percentage of seniors with cars, both referenced in the premise
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of'seniors_premise'
    label = "contradiction"
elif car_percentage_hypothesis!= car_percentage_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)