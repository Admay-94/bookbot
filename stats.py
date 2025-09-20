def get_num_words(text):
    return len(text.split())        

def get_num_chars(text):
    lowered = text.lower()
    counts = {}
    
    for ch in lowered:
      if ch in counts:
        counts[ch] += 1
      else:
        counts[ch] = 1
    return counts

def sort_on(item):
  return item["num"]

def build_sorted_letters(char_counts):

  letters = []

  for ch, cnt in char_counts.items():
    letters.append({"char": ch, "num": cnt})
  letters.sort(reverse=True, key=sort_on)
  return letters

