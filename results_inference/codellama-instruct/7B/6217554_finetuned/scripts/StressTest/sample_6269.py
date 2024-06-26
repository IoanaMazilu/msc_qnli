death_rate_premise = 10
death_rate_hypothesis = 10
fear_rate_premise = 20
fear_rate_hypothesis = 20

# the hypothesis talks about the death and fear rates in the village, referenced also in the premise
if death_rate_hypothesis > death_rate_premise:
    # check if the hypothesis value contradicts the death rate in the premise
    label = "contradiction"
elif fear_rate_hypothesis!= fear_rate_premise:
    # check if the fear rate in the hypothesis contradicts the fear rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
