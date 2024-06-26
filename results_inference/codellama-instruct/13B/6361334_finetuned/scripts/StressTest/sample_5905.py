cookies_premise = 7/8
cookies_hypothesis = 1/8
half_premise = 1/2
half_hypothesis = 1/2
tyler_premise = 150
tyler_hypothesis = 150

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler, mentioned in the premise
if cookies_hypothesis!= cookies_premise:
    # check if the hypothesis value contradicts the number of cookies eaten by Michael in the premise
    label = "contradiction"
elif half_hypothesis!= half_premise:
    # check if the hypothesis value contradicts the number of cookies eaten by Steve in the premise
    label = "contradiction"
elif tyler_hypothesis!= tyler_premise:
    # check if the hypothesis value contradicts the number of cookies eaten by Tyler in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
