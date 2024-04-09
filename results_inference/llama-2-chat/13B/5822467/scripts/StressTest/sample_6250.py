boys_premise = 5
girls_premise = 4
committee_size_premise = 4

boys_hypothesis = 6
girls_hypothesis = 4
committee_size_hypothesis = 4

# the hypothesis refers to the number of boys and girls in the committee and the committee size
if boys_hypothesis <= boys_premise and girls_hypothesis <= girls_premise and committee_size_hypothesis == committee_size_premise:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
elif boys_hypothesis > boys_premise or girls_hypothesis > girls_premise or committee_size_hypothesis!= committee_size_premise:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys and girls in the committee and the committee size
    # any number of boys and girls greater than or equal to 'boys_premise' and 'girls_premise' and any committee size greater than or equal to 'committee_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
