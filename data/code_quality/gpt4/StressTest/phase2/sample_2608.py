men_diff_premise = 6
men_diff_hypothesis = 4
women_diff_premise = 6
women_diff_hypothesis = 6

# the hypothesis refers to the difference in number of men and women between Snyder and Leigh
if men_diff_hypothesis >= men_diff_premise:
    # check if the hypothesis value contradicts the premise's statement of 'less than men_diff_premise'
    label = "contradiction"
elif women_diff_hypothesis != women_diff_premise:
    # check if the number of additional women in Snyder's choir in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment 
    label = "entailment"

print(label)
