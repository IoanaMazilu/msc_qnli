cookies_michael_premise = 1/8
cookies_michael_hypothesis = 1/8
cookies_steve_premise = 1/2
cookies_steve_hypothesis = 1/2
cookies_tyler_premise = 150
cookies_tyler_hypothesis = 150

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler mentioned in the premise
if cookies_michael_premise <= cookies_michael_hypothesis:
    # check if the estimate of 'cookies_michael_hypothesis' contradicts the number of cookies eaten by Michael in the premise
    label = "contradiction"
elif cookies_steve_hypothesis!= cookies_steve_premise:
    # check if the number of cookies eaten by Steve in the hypothesis contradicts the number of cookies eaten by Steve reported in the premise
    label = "contradiction"
elif cookies_tyler_hypothesis!= cookies_tyler_premise:
    # check if the number of cookies eaten by Tyler in the hypothesis contradicts the number of cookies eaten by Tyler reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
