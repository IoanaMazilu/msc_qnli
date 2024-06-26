cookies_premise = 1/8
cookies_hypothesis = 1/8
half_steve_ate_premise = 1/2
half_steve_ate_hypothesis = 1/2
tyler_ate_more_premise = 150
tyler_ate_more_hypothesis = 150

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler
if cookies_hypothesis <= cookies_premise:
    # check if the estimate of 'cookies_hypothesis' contradicts the number of cookies eaten by Michael in the premise
    label = "contradiction"
elif half_steve_ate_hypothesis!= half_steve_ate_premise:
    # check if the number of cookies eaten by Steve in the hypothesis contradicts the number of cookies eaten by Steve reported in the premise
    label = "contradiction"
elif tyler_ate_more_hypothesis!= tyler_ate_more_premise:
    # check if the number of cookies eaten by Tyler in the hypothesis contradicts the number of cookies eaten by Tyler reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
