ysoserial_premise_1 = 300
ysoserial_hypothesis_1 = 300
percentage_premise = 50
percentage_hypothesis = 50

# the hypothesis refers to the number of seniors and the percentage of seniors with cars, both mentioned in the premise
if ysoserial_hypothesis_1!= ysoserial_premise_1:
    # check if the number of seniors in the hypothesis contradicts the number of seniors in the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

