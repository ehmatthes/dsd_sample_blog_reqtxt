"""Update the requirements for the sample project.

- This assumes uv is available.
- Uses uv to resolve requirements, but `pip download` to populate vendor/.
- uv does not currently support `pip download` (12/2/24).
  See: https://github.com/astral-sh/uv/issues/3163
"""

from pathlib import Path
import subprocess

# --- Update requirements.txt ---
path_root = Path(__file__).parent
path_req_in = path_root  / "requirements.in"
path_req_txt = path_root / "requirements.txt"

assert path_req_in.exists()
assert path_req_txt.exists()

cmd_simple = f"uv pip compile {path_req_in.as_posix()}"#" > {path_req_txt.as_posix()}"
cmd = f"uv pip compile {path_req_in.as_posix()} > {path_req_txt.as_posix()}"
subprocess.run(cmd, shell=True)

# Remove comments, because they just get in the way of testing.
lines_req_txt = path_req_txt.read_text().splitlines()
lines_req_txt = [l for l in lines_req_txt if "#" not in l]
contents = "\n".join(lines_req_txt) + "\n"
path_req_txt.write_text(contents)
