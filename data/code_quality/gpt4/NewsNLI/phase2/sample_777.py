guests_premise = 200
guests_hypothesis = 1000

# the hypothesis implies that the number of guests at a wedding in Nigeria is greater than what is stated in the premise
if guests_hypothesis <= guests_premise:
    # check if the number of guests in the hypothesis contradicts the number of guests in the premise
    label = "contradiction"
else:
    # if the number of guests in the hypothesis does not contradict, but is greater than the number of guests in the premise, we infer neutrality
    label = "neutral"

print(label)
