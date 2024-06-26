neha_premise = 10
neha_hypothesis = 10

sonali_premise = 15
priyanka_premise = 15

sadaf_premise = 10
tanu_premise = 10

# The hypothesis is about the age of Neha, Sonali, Priyanka, Sadaf, and Tanu which is also mentioned in the premise.
if neha_hypothesis > neha_premise:
    # The hypothesis suggests that Neha is less than 10 which contradicts the premise where Neha is 10.
    label = "contradiction"
else:
    # If Neha's age does not contradict the premise, we infer entailment as all other ages are the same as in the premise
    label = "entailment"

print(label)
