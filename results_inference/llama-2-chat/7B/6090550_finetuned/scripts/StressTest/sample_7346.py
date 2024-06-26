percent_drop_premise = 28
percent_drop_hypothesis = 28
percent_rally_premise = 5
percent_rally_hypothesis = 5

# the hypothesis talks about the same percentage drop and rally in crude oil prices
if percent_drop_hypothesis!= percent_drop_premise:
    label = "contradiction"
elif percent_rally_hypothesis!= percent_rally_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
