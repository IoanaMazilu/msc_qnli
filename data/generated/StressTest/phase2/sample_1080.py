# Premise: If neha is 10 Both Sonali and priyanka is 15 Both sadaf and tanu is 10. how much is prinka by the same system?
# Hypothesis: If neha is less than 70 Both Sonali and priyanka is 15 Both sadaf and tanu is 10. how much is prinka by the same system?
# Golden Label: entailment

neha_premise = 10
neha_hypothesis = 70
sonali_priyanka_premise = 15
sonali_priyanka_hypothesis = 15
sadaf_tanu_premise = 10
sadaf_tanu_hypothesis = 10

# the hypothesis talks about the values of Neha, Sonali, Priyanka, Sadaf, and Tanu, which are also mentioned in the premise
if neha_hypothesis > neha_premise:
    # check if the value of 'neha_hypothesis' contradicts the value of Neha in the premise
    label = "contradiction"
elif sonali_priyanka_hypothesis != sonali_priyanka_premise or sadaf_tanu_hypothesis != sadaf_tanu_premise:
    # check if the values of Sonali, Priyanka, Sadaf, and Tanu in the hypothesis contradict the values in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

