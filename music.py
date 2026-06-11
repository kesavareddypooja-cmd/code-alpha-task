import random

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

generated_music = []

for i in range(10):
    generated_music.append(random.choice(notes))

print("Generated Music Notes:")
print(" ".join(generated_music))
