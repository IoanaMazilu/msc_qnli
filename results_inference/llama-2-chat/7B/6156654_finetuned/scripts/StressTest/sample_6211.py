men_premise = 600
men_hypothesis = 100
km_premise = 2
km_hypothesis = 2
days_premise = 50
days_hypothesis = 50
hours_premise = 8
hours_hypothesis = 8

# the hypothesis talks about the number of men and distance, which are also mentioned in the premise
if men_hypothesis > men_premise:
    # check if the number of men in the hypothesis contradicts the number of men in the premise
    label = "contradiction"
elif km_hypothesis!= km_premise or days_hypothesis!= days_premise or hours_hypothesis!= hours_premise:
    # check if the distance, days and hours in the hypothesis contradict the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
