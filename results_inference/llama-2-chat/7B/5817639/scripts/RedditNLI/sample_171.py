premise = "UK Disposable Income Falls Most In Peacetime Since 1921."
hypothesis = "UK disposable income falls to lowest since 1921."

# compare the premise and hypothesis dates
date_premise = datetime.strptime(premise, "%B %Y")
date_hypothesis = datetime.strptime(hypothesis, "%B %Y")

# check if the dates in the hypothesis contradict the dates in the premise
if date_hypothesis < date_premise:
    label = "contradiction"
else:
    # the premise and hypothesis mention the same time period, so we can compare the rest of the information
    # check if the amount of disposable income in the hypothesis contradicts the premise amount
    if hypothesis.lower()!= "uk disposable income falls to lowest since 1921":
        label = "contradiction"
    else:
        label = "entailment"

print(label)
