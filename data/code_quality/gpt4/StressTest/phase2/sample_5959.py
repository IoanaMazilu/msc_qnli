eng_fr_travelers_premise = 8
eng_fr_travelers_hypothesis = 6

eng_it_travelers_premise = 0
eng_it_travelers_hypothesis = 0

fr_it_travelers_premise = 11
fr_it_travelers_hypothesis = 11

# the hypothesis refers to the number of club members who traveled to the same countries mentioned in the premise
if eng_fr_travelers_hypothesis >= eng_fr_travelers_premise:
    # check if the hypothesis value contradicts the estimate of less than 'eng_fr_travelers_premise'
    label = "contradiction"
elif eng_it_travelers_hypothesis != eng_it_travelers_premise:
    # check if the number of members who traveled to England and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif fr_it_travelers_hypothesis != fr_it_travelers_premise:
    # check if the number of members who traveled to France and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
