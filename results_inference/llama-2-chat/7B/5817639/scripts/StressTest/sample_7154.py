highlighter_premise = {
    "pink": 9,
    "yellow": 8,
    "blue": 5
}

highlighter_hypothesis = {
    "pink": 3,
    "yellow": 8,
    "blue": 5
}

# the hypothesis talks about the number of highlighters of each color in a desk, referenced also in the premise
if highlighter_hypothesis["pink"] <= highlighter_premise["pink"] or highlighter_hypothesis["yellow"] <= highlighter_premise["yellow"] or highlighter_hypothesis["blue"] <= highlighter_premise["blue"]:
    # check if the hypothesis value contradicts the estimate of more than 'highlighter_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of highlighters
    # any number of highlighters of each color greater than 'highlighter_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
