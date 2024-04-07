# Premise: If Snyder has less than 5 more men and 6 more women than Leigh, how many women are in the Snyder choir?
# Hypothesis: If Snyder has 4 more men and 6 more women than Leigh, how many women are in the Snyder choir?
# Golden Label: neutral

men_difference_premise = 5
men_difference_hypothesis = 4
women_difference_premise = 6
women_difference_hypothesis = 6

# the hypothesis talks about the difference of men and women in the Snyder choir compared to Leigh's choir, same as the premise
if men_difference_hypothesis >= men_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'men_difference_premise'
    label = "contradiction"
elif women_difference_hypothesis != women_difference_premise:
    # check if the number of women in the hypothesis contradicts the number of women reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

