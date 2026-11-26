import random


class EmptyScoreError(ValueError):
    def __init__(self):
        super().__init__("No random scores were generated for the output file")


def save_random_scores(filename, count):
    try:
        scores = [random.randint(1, 100) for _ in range(count)]
        if not scores:
            raise EmptyScoreError
        with open(filename, "w") as file:
            for score in scores:
                if score > 50 and score % 2 == 0:
                    file.write(f"High even score: {score}\n")

    except FileNotFoundError as e:
        print(f"Failed: {e}")
        raise RuntimeError("Logging failed")
