boys_premise = 6
girls_premise = 4
committee_premise = 4
boys_hypothesis = 2
girls_hypothesis = 4
committee_hypothesis = 4

# the hypothesis refers to the number of boys, girls and committee members mentioned in the premise
if boys_hypothesis > boys_premise or girls_hypothesis > girls_premise:
    # check if the number of boys or girls in the hypothesis exceeds the number in the premise
    label = "contradiction"
elif committee_hypothesis > committee_premise:
    # check if the number of committee members in the hypothesis exceeds the number in the premise
    label = "contradiction"
elif boys_hypothesis < boys_premise and girls_hypothesis == girls_premise and committee_hypothesis == committee_premise:
    # if the number of boys in the hypothesis is less than the number in the premise, but the number of girls and committee members is the same, we can infer neutrality
    label = "neutral"
else:
    # if none of the above conditions are met, we can infer entailment
    label = "entailment"

print(label)
