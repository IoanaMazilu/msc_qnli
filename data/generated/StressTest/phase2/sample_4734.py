# Premise: If Snyder has 4 more men and 6 more women than Leigh, how many men are in the Snyder choir?
# Hypothesis: If Snyder has less than 7 more men and 6 more women than Leigh, how many men are in the Snyder choir?
# Golden Label: entailment

men_difference_premise = 4
men_difference_hypothesis = 7
women_difference_premise = 6
women_difference_hypothesis = 6

# the hypothesis refers to the difference in the number of men and women between Snyder and Leigh mentioned in the premise
if men_difference_premise >= men_difference_hypothesis:
    # check if the estimated 'men_difference_hypothesis' contradicts the number of men difference in the premise
    label = "contradiction"
elif women_difference_premise != women_difference_hypothesis:
    # check if the number of women difference in the hypothesis contradicts the number of women difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

