# Premise: Christine and Siri have 21 rs between them.
# Hypothesis: Christine and Siri have less than 81 rs between them.
# Golden Label: entailment

money_premise = 21
money_hypothesis = 81

# the hypothesis talks about the total money Christine and Siri have, which is also mentioned in the premise
if money_premise > money_hypothesis:
    # check if the amount of money in the premise contradicts the hypothesis estimate of less than 'money_hypothesis'
    label = "contradiction"
elif money_hypothesis != money_premise:
    # check if the amount of money mentioned in the hypothesis contradicts the exact amount of money reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

