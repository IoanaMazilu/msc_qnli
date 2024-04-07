# Premise: Gordon buys 5 dolls for his 5 nieces.
# Hypothesis: Gordon buys more than 5 dolls for his 5 nieces.
# Golden Label: contradiction

dolls_bought_premise = 5
dolls_bought_hypothesis = 5
nieces_premise = 5
nieces_hypothesis = 5

# the hypothesis refers to the number of dolls bought and nieces mentioned in the premise
if dolls_bought_hypothesis != dolls_bought_premise:
    # check if the assertion of 'dolls_bought_hypothesis' contradicts the number of dolls bought in the premise
    label = "contradiction"
elif nieces_hypothesis != nieces_premise:
    # check if the number of nieces in the hypothesis contradicts the number of nieces reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"

print(label)

