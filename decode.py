import glob
import os


def decode(dir="Custom"):
    for filepath in glob.glob(dir + "/*"):
        if os.path.isdir(filepath):
            continue

        with open(filepath, "rb") as f:
            content = f.read()
            if content.startswith(b"UnityFS"):
                # Find the second occurrence of "UnityFS" in the file
                index = content.find(b"UnityFS", 1)
                if index == -1:
                    print(f"Skipping already decoded {filepath}")
                else:
                    print(f"Decoding {filepath}")
                    with open(filepath, "wb") as f:
                        f.write(content[index:])
            else:
                print(f"Skipping {filepath}")


if __name__ == "__main__":
    decode()
