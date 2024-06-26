# define variables for the numerical entities in the premise and hypothesis
hours_dan_works = 6
hours_annie_works = None

# extract the quantities as valid numbers
if "hours" in premise:
    hours_dan_works = int(premise.split("hours")[0])
if "hours" in hypothesis:
    hours_annie_works = int(hypothesis.split("hours")[0])

# check if the hypothesis value contradicts the premise value
if hours_annie_works is not None and hours_annie_works < hours_dan_works:
    label = "contradiction"
else:
    label = "neutral"

print(label)
