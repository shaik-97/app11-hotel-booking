import subprocess
import sys
from pathlib import Path


def compile_c_file(c_file: str, output_name: str | None = None) -> int:
    """Compile a C source file using the system C compiler."""
    source = Path(c_file)

    if not source.exists():
        print(f"Error: file not found -> {c_file}")
        return 1

    if not source.name.endswith(".c"):
        print(f"Error: expected a .c file, got -> {source.name}")
        return 1

    if output_name is None:
        output_name = source.stem

    compiler = "gcc"
    command = [compiler, source.name, "-o", output_name]

    print(f"Compiling: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

    if result.returncode == 0:
        print(f"Compilation successful. Output: {output_name}")
    else:
        print("Compilation failed.")

    return result.returncode


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python c_compiler.py <your_file.c> [output_name]")
        sys.exit(1)

    output = sys.argv[2] if len(sys.argv) > 2 else None
    sys.exit(compile_c_file(sys.argv[1], output))
