# Premise: Ticket sales for maiden passenger trip between Singapore and Sydney Top ticket price:US$100,380 The bargain:US$560 for a single economy seat E-mail to a friend.
# Hypothesis: One passenger paid $100,000 for the first Singapore to Sydney trip.
# Golden Label: neutral

top_ticket_price_premise = 100380
top_ticket_price_hypothesis = 100000

# the hypothesis mentions the top ticket price for the first trip from Singapore to Sydney, which is also referenced in the premise
if top_ticket_price_hypothesis > top_ticket_price_premise:
    # check if the top ticket price in the hypothesis contradicts the top ticket price reported in the premise
    label = "contradiction"
elif top_ticket_price_hypothesis < top_ticket_price_premise:
    # check if the top ticket price from the hypothesis is less than the top ticket price in the premise
    label = "entailment"
else:
    # if the hypothesis top ticket price value does not contradict the premise top ticket price, we can infer neutrality
    label = "neutral"

print(label)

