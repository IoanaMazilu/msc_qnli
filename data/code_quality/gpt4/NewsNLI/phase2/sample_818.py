percentage_same_sex_marriage_legal_premise = 0.72
states_same_sex_marriage_legal_hypothesis = 37
total_us_states = 50

# the hypothesis mentions the number of states where same-sex marriage is legal
# whereas the premise mentions the percentage of people living in states where same-sex marriage is legal
# we need to calculate the percentage of states allowing same-sex marriage mentioned in the hypothesis
percentage_states_same_sex_marriage_legal_hypothesis = states_same_sex_marriage_legal_hypothesis / total_us_states

if percentage_states_same_sex_marriage_legal_hypothesis != percentage_same_sex_marriage_legal_premise:
    # check if the percentage of states allowing same-sex marriage from the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage from the hypothesis does not contradict the percentage from the premise, we can infer entailment
    label = "entailment"

print(label)
