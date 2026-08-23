import subprocess


def on_config(config):
    def git(*args):
        return subprocess.check_output(
            ["git", *args],
            text=True
        ).strip()

    config.extra["commit_sha"] = git("rev-parse", "--short", "HEAD")
    config.extra["commit_message"] = git("log", "-1", "--pretty=%s")
    config.extra["commit_url"] = (
        "https://github.com/thommyho/Cpp-gRPC-Windows-PreBuilts/commit/"
        + git("rev-parse", "HEAD")
    )

    return config