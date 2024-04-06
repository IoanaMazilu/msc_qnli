# Premise: '' Not only was this defendant untruthful on his application to the University and his numerous scholarship applications, he is also alleged to have stolen over $45,000 in grants, scholarship and financial aid money awarded to him on applications and submissions of documents that were based on lies and reproductions of other people's hard work,'' Leone said.
# Hypothesis: Wheeler accused of stealing more than $45,000 in grants, financial aid.
# Golden Label: neutral

stolen_money_premise = 45000
stolen_money_hypothesis = 45000

# the hypothesis mentions the amount of money allegedly stolen by the defendant, which is also mentioned in the premise
if stolen_money_hypothesis != stolen_money_premise:
    # check if the stolen money amount in the hypothesis contradicts the stolen money amount reported in the premise
    label = "contradiction"
else:
    # if the stolen money amount in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

