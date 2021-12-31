import os


def _highscore_static_init(cls):
    cls._setup_highscore()
    return cls


@_highscore_static_init
class Score:
    score = 0
    # Initialized statically
    highscore = None
    prev_highscore = None

    @staticmethod
    def add_points(points):
        Score.score += points
        if Score.score > Score.prev_highscore:
            Score.highscore = Score.score

    @staticmethod
    def overwrite_highscore():
        if Score.highscore > Score.prev_highscore:
            with open(".env", "w") as file:
                file.write(f"HIGHSCORE2048={Score.highscore}")

    @classmethod
    def _setup_highscore(cls):
        if not os.path.exists(".env"):
            with open(".env", "w+") as file:
                file.write("HIGHSCORE2048=0")
                setattr(cls, "prev_highscore", 0)
                setattr(cls, "highscore", 0)
        else:
            with open(".env") as file:
                score = int(file.readline().split("=")[-1])
                setattr(cls, "prev_highscore", score)
                setattr(cls, "highscore", score)
