num_women_premise = 4
num_men_premise = 4
num_women_hypothesis = 6
num_men_hypothesis = 6

# the hypothesis refers to the number of women and men on the board of education
if num_women_hypothesis > num_women_premise:
    # check if the hypothesis value contradicts the number of women in the premise
    label = "contradiction"
elif num_men_hypothesis > num_men_premise:
    # check if the hypothesis value contradicts the number of men in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
