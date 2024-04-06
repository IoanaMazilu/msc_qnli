# Premise: The country's general prosecutor ordered Morsy to stand trial along with 14 members of the Muslim Brotherhood, the news agency said.
# Hypothesis: 14 members of the Muslim Brotherhood are also ordered to stand trial.
# Golden Label: entailment

members_premise = 14
members_hypothesis = 14

# the hypothesis mentions the number of Muslim Brotherhood members ordered to stand trial, which is also mentioned in the premise
if members_hypothesis != members_premise:
    # check if the number of members in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
else:
    # if the number of members in the hypothesis does not contradict the number of members in the premise, we can infer entailment
    label = "entailment"

print(label)

