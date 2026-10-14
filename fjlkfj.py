import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--name", type = str, help = "Name of the file")
args = parser.parse_args()
print(f"file name: {args.name}")