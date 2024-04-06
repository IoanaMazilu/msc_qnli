# Premise: SENSEX rallied 500 points, Tata motors up 8.01%, Today Nifty future stock trading call on Tuesday 10 Sept, Indian share market tips.
# Hypothesis: Sensex & Nifty down, Global market update today, Indian share nifty future trading call on Wednesday 11 Sept, Free Stock future call.
# Golden Label: contradiction

points_premise = 500
percentage_increase_premise = 8.01
day_premise = 10

points_hypothesis = None
percentage_increase_hypothesis = None
day_hypothesis = 11

# the premise and hypothesis mention the change in SENSEX points and Tata motors percentage, and the day of the trading call
if points_hypothesis is not None and points_hypothesis > points_premise:
    # check if the change in SENSEX points in the hypothesis contradicts the change in SENSEX points in the premise
    label = "contradiction"
elif percentage_increase_hypothesis is not None and percentage_increase_hypothesis < percentage_increase_premise:
    # check if the change in Tata motors percentage in the hypothesis contradicts the change in Tata motors percentage in the premise
    label = "contradiction"
elif day_hypothesis != day_premise:
    # check if the day of the trading call in the hypothesis contradicts the day of the trading call in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

