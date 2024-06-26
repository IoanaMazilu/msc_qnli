guests_premise = 200
guests_hypothesis = 200

# the hypothesis mentions the number of people George H.W. Bush will celebrate his birthday with, which is also referenced in the premise
# however, the hypothesis does not mention the performance by Ronan Tynan, which is mentioned in the premise
if guests_hypothesis != guests_premise:
    # check if the number of guests in the hypothesis contradicts the number of guests mentioned in the premise
    label = "contradiction"
else:
    # if the number of guests from the hypothesis does not contradict the number of guests in the premise, we can infer neutrality
    label = "neutral"

print(label)
