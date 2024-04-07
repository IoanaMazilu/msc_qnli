# Premise: If less than 86 of the photographs in the exhibition were taken by Octavia, how many photographs were either framed by Jack or taken by Octavia?
# Hypothesis: If 36 of the photographs in the exhibition were taken by Octavia, how many photographs were either framed by Jack or taken by Octavia?
# Golden Label: neutral

photos_taken_by_octavia_premise = 86
photos_taken_by_octavia_hypothesis = 36

# the hypothesis talks about the number of photos taken by Octavia, referenced also in the premise
if photos_taken_by_octavia_hypothesis >= photos_taken_by_octavia_premise:
    # check if the hypothesis value contradicts the premise of less than 'photos_taken_by_octavia_premise'
    label = "contradiction"
elif photos_taken_by_octavia_hypothesis < photos_taken_by_octavia_premise:
    # the premise gives only an estimate for the number of photos taken by Octavia
    # any number of photos less than 'photos_taken_by_octavia_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

