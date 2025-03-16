scores = input("Enter student scores::\n").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])

print(type(scores))
max_score = 0

for score in scores:
    if score > max_score:
        max_score = score

print(f"The highest number is:: {max_score}")


