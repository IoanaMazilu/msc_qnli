num_women_premise = 4
num_men_premise = 4
num_women_hypothesis = 1
num_men_hypothesis = 1

# the hypothesis refers to the number of women and men on the board of education, mentioned in the premise
if num_women_hypothesis!= num_women_premise:
    # check if the number of women in the hypothesis contradicts the number of women in the premise
    label = "contradiction"
elif num_men_hypothesis!= num_men_premise:
    # check if the number of men in the hypothesis contradicts the number of men in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
