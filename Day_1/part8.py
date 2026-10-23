scores = [70, 85, 90]
scores.append(95)
print(scores)
scores[0] = 75
print(scores)
scores.remove(85)
print(scores)
print("Count:", len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))