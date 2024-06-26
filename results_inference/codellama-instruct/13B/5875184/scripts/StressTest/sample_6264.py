# define variables for the numerical entities in the premise and hypothesis
hours_dan_works = 3
hours_annie_works = 2

# check if the hypothesis value contradicts the premise value
if hours_dan_works <= hours_annie_works:
    label = "contradiction"
else:
    label = "neutral"

print(label)
