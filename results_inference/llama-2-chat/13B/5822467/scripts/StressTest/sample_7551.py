boys_premise = 6
girls_premise = 4
committee_size_premise = 4

boys_hypothesis = "more than 2"
girls_hypothesis = 4

# the hypothesis talks about the number of boys and girls in the group
if boys_hypothesis <= boys_premise and girls_hypothesis <= girls_premise:
    # check if the hypothesis values contradict the number of boys and girls reported in the premise
    label = "contradiction"
elif boys_hypothesis > boys_premise or girls_hypothesis > girls_premise:
    # check if the number of boys or girls in the hypothesis contradicts the number of boys and girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
