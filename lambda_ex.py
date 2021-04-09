def run():  
  palindrome = lambda word: word == word[::-1]

  name = input("Type a word: ")
  print(palindrome(name))

if __name__ == '__main__':
  run()