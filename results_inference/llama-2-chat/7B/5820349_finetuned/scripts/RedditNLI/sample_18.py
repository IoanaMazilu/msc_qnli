sensex_pts_premise = 362.75
nifty_pts_premise = None

sensex_pts_hypothesis = 357.39
nifty_pts_hypothesis = None

# the hypothesis and premise mention the points of the Sensex and Nifty closures
if sensex_pts_premise!= sensex_pts_hypothesis:
    # check if the points of the Sensex in the hypothesis contradicts the points of the Sensex in the premise
    label = "contradiction"
elif nifty_pts_premise is None or nifty_pts_hypothesis is None:
    # the premise does not mention the points of the Nifty, so we cannot check for contradiction
    label = "neutral"
else:
    # if the points of the Sensex in the hypothesis do not contradict the points of the Sensex in the premise, and the points of the Nifty are equal, we can infer entailment
    label = "entailment"

print(label)
