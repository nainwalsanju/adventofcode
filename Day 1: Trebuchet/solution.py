def process_file(file_path):
  try:
    sum = 0
    with open(file_path, "r") as file:
      for line in file:
        # print(line.strip())
        sum += int(create_two_digit_number(line.strip()))
        # print(sum)
    print(sum)
  except FileNotFoundError:
    print(f"File '{file_path}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")


def create_two_digit_number(input_string) -> str:
  first_digit = ""
  last_digit = ""
  for char in input_string:
    if char.isdigit():
      if first_digit == "":
        first_digit = char
      last_digit = char
  return first_digit + last_digit


def main():
  file_path = "input.txt"
  process_file(file_path)


if __name__ == "__main__":
  main()
