import subprocess

sentences = [
    "The dog chased the ball quickly.",
    "Birds fly south in winter."
]

for sentence in sentences:
    print(f"\nSentence: {sentence}")
    print("-" * 50)
    result = subprocess.run(
        ["link-parser"],
        input=sentence + "\n!quit\n",
        capture_output=True,
        text=True
    )
    print(result.stdout)
