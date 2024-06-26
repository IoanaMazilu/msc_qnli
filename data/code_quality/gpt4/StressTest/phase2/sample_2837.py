neha_premise = 10
neha_hypothesis = 10

sonali_premise = 15
priyanka_premise = 15

sadaf_premise = 10
tanu_premise = 10

# the hypothesis talks about the values of neha, sonali, priyanka, sadaf and tanu, also mentioned in the premise
if neha_hypothesis > neha_premise:
    # check if the value of 'neha_hypothesis' contradicts the value of neha in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
