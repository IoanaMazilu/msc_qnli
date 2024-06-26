us_rank_premise = 36
math_score_premise = 481
countries_assessed_hypothesis = 65

# the hypothesis mentions the US ranking below average for all 65 countries assessed
# the premise provides the US rank and score in mathematics but does not specify the total number of countries assessed
if us_rank_premise > countries_assessed_hypothesis / 2:
    # check if the US rank from the premise is below the average rank from the hypothesis
    label = "entailment"
else:
    # if the US rank from the premise is not below the average rank from the hypothesis, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
