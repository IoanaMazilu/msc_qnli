seniors_premise = 300
seniors_hypothesis = 800
percentage_premise = 40
percentage_hypothesis = 40

# the hypothesis talks about the number of seniors and percentage of seniors with cars, which are also mentioned in the premise
if seniors_hypothesis <= seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the number of seniors in the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
