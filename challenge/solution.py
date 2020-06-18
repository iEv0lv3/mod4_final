payload = [1, 3, 4, 5, 6, 2, 3, 4, 1]
target = 5

def find_target(payload, target):
  number_dict = {}
  pairs = []
  for num in payload:
      number_dict[num] = number_dict.get(num, 0) + 1
      complement = target - num
      if complement in number_dict:
          pairs.append((num, complement))
          break
  return pairs

print(find_target(payload, target))
