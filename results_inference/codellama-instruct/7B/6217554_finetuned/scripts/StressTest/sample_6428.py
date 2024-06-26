cookies_sold_premise = 450
cookies_sold_hypothesis = 750

# the hypothesis talks about the number of cookies sold, referenced also in the premise
if cookies_sold_hypothesis!= cookies_sold_premise:
    # check if the number of cookies sold in the hypothesis contradicts the number of cookies sold reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
