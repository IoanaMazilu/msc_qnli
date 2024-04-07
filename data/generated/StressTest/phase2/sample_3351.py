# Premise: From a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: From a group of more than 4 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: entailment

boys_premise = 6
boys_hypothesis = 4
girls_premise = 4
girls_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis talks about the number of boys and girls in a group and the members of a committee,
# all these aspects are also referenced in the premise
if boys_hypothesis > boys_premise:
    # check if the estimate of 'boys_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif girls_hypothesis != girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls mentioned in the premise
    label = "contradiction"
elif committee_hypothesis != committee_premise:
    # check if the number of committee members in the hypothesis contradicts the number of committee members in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

