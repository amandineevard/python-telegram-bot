import os    
files_no_ext = [".".join(f.split(".")[:-1]) for f in os.listdir() if os.path.isfile(f)]
print(files_no_ext)

__all__ = [
    "start_command",
    "help_command",
    "random_joke_command",
    "random_insult_command",
    "love_calculator_command",
    "ok_boomer_command",
    "random_reddit_command",
    "judge_poll_command",
    "spongebob",
]
