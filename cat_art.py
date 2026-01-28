from datetime import datetime, timedelta
import subprocess, os

CAT = [
    [0,1,0,1,0],
    [1,0,1,0,1],
    [1,1,1,1,1],
    [1,0,1,0,1],
    [0,1,1,1,0],
]

FRAMES = [0, 2, 4, 6, 8]  # movement across weeks
START_DATE = datetime(2025, 1, 6)  # Monday

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for frame in FRAMES:
    for row in range(len(CAT)):
        for col in range(len(CAT[0])):
            if CAT[row][col] == 1:
                commit_date = START_DATE + timedelta(
                    weeks=frame + col,
                    days=row
                )

                with open("cat.txt", "a", encoding="utf-8") as f:
                    f.write(f"🐱 {commit_date.date()}\n")

                env = os.environ.copy()
                env["GIT_AUTHOR_DATE"] = commit_date.isoformat()
                env["GIT_COMMITTER_DATE"] = commit_date.isoformat()

                subprocess.run(["git", "add", "cat.txt"], env=env)
                subprocess.run(
                    ["git", "commit", "-m", f"Walking cat {frame}-{row}-{col}"],
                    env=env
                )
