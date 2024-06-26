seniors_premise = 300
seniors_hypothesis = 500
percentage_premise = 50
percentage_hypothesis = 50

# the hypothesis talks about the number of seniors and the percentage of seniors with cars, which are also mentioned in the premise
if seniors_premise!= seniors_hypothesis:
    # check if the number of seniors in the hypothesis contradicts the number of seniors in the premise
    label = "contradiction"
elif percentage_premise!= percentage_hypothesis:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
