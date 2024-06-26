points_premise = 500
percentage_premise = 8.01
nifty_future_premise = 10
nifty_future_hypothesis = 11

# the hypothesis and premise mention the points and percentage increase of SENSEX and NIFTY
# the hypothesis also mentions the date of the NIFTY future call and the stock market update
# the premise does not mention the date of the NIFTY future call or the stock market update
# the premise does not mention any decrease in SENSEX or NIFTY
# the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
label = "neutral"

print(label)
