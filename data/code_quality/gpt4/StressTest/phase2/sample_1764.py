men_diff_premise = 4
men_diff_hypothesis = 5
women_diff_premise = 6
women_diff_hypothesis = 6

# the hypothesis talks about the difference of men and women in Snyder and Leigh choirs
if men_diff_premise >= men_diff_hypothesis:
    # check if 'men_diff_premise' contradicts the hypothesis that Snyder has less than 'men_diff_hypothesis' more men than Leigh
    label = "contradiction"
elif women_diff_premise != women_diff_hypothesis:
    # check if the difference in number of women in Snyder and Leigh choirs contradicts the difference reported in the hypothesis
    label = "contradiction"
else:
    # if the differences in the men and women numbers do not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
