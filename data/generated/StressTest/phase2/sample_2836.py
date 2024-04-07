# Premise: If neha is less than 60 Both Sonali and priyanka is 15 Both sadaf and tanu is 10. how much is prinka by the same system?
# Hypothesis: If neha is 10 Both Sonali and priyanka is 15 Both sadaf and tanu is 10. how much is prinka by the same system?
# Golden Label: neutral

neha_premise = 60
neha_hypothesis = 10
sonali_priyanka_premise = 15
sonali_priyanka_hypothesis = 15
sadaf_tanu_premise = 10
sadaf_tanu_hypothesis = 10

# the hypothesis compares neha, sonali, priyanka, sadaf and tanu's values with those in the premise
if neha_hypothesis >= neha_premise:
    # check if the value of 'neha_hypothesis' contradicts the value of neha in the premise
    label = "contradiction"
elif sonali_priyanka_hypothesis != sonali_priyanka_premise:
    # check if the value of sonali and priyanka in the hypothesis contradicts their value in the premise
    label = "contradiction"
elif sadaf_tanu_hypothesis != sadaf_tanu_premise:
    # check if the value of sadaf and tanu in the hypothesis contradicts their value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

