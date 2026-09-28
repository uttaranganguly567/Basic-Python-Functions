def count_occurence(text):
  counts = [0, 0, 0, 0, 0]
  for i in range (len(text)):
    match(text[i]):
      case 'a':
        counts[0] += 1
      case 'e':
        counts[1] += 1
      case 'i':
        counts[2] += 1
      case 'o':
        counts[3] += 1
      case 'u':
        counts[4] += 1

  print(f"a: {counts[0]}")
  print(f"e: {counts[1]}")
  print(f"i: {counts[2]}")
  print(f"o: {counts[3]}")
  print(f"u: {counts[4]}")


count_occurence(input("Enter text: "))