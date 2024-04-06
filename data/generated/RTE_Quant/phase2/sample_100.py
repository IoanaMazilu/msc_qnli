# Premise: In Baghdad, a car bomb exploded late Sunday near a police patrol in the fashionable Jadiriyah district, killing at least six people, including three police officers, and wounding 26 others.
# Hypothesis: The bomb killed six people, including three policeman.
# Golden Label: entailment

total_killed_premise = 6
police_killed_premise = 3
total_killed_hypothesis = 6
police_killed_hypothesis = 3

# the hypothesis talks about the total number of people and police officers killed, which is also mentioned in the premise
if total_killed_hypothesis != total_killed_premise:
    # check if the total number of people killed in the hypothesis contradicts the total number of people killed in the premise
    label = "contradiction"
elif police_killed_hypothesis != police_killed_premise:
    # check if the number of police officers killed in the hypothesis contradicts the number of police officers killed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

