boys_premise = 6
girls_premise = 4
committee_size_premise = 4

boys_hypothesis = 7
girls_hypothesis = 5
committee_size_hypothesis = 4

# the hypothesis refers to the number of boys and girls in the committee and the committee size
if boys_hypothesis <= boys_premise and girls_hypothesis <= girls_premise and committee_size_hypothesis == committee_size_premise:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
elif boys_hypothesis > boys_premise or girls_hypothesis > girls_premise or committee_size_hypothesis!= committee_size_premise:
    # the hypothesis values contradict the premise ones, we can infer contradiction
    label = "contradiction"
else:
    # the premise only gives an estimate for the number of boys and girls, and the committee size
    # any number of boys and girls greater than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
