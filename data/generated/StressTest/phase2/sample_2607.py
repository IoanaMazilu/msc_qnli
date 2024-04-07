# Premise: If Snyder has 4 more men and 6 more women than Leigh, how many women are in the Snyder choir?
# Hypothesis: If Snyder has less than 6 more men and 6 more women than Leigh, how many women are in the Snyder choir?
# Golden Label: entailment

men_difference_premise = 4
men_difference_hypothesis = 6
women_difference_premise = 6
women_difference_hypothesis = 6

# the hypothesis refers to the difference in numbers of men and women between Snyder and Leigh mentioned in the premise
if men_difference_hypothesis >= men_difference_premise:
    # check if the difference of men in the hypothesis contradicts the difference of men in the premise
    label = "contradiction"
elif women_difference_hypothesis != women_difference_premise:
    # check if the difference of women in the hypothesis contradicts the difference of women in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

