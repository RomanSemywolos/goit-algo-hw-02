from collections import deque

def is_palindrome(text):

    result = ''

    text = text.lower()
    is_pal_deque = deque()
    for char in text:
        if char.isalpha():
            is_pal_deque.append(char)

    while len(is_pal_deque) > 1:
       first_char = is_pal_deque.pop()
       last_char = is_pal_deque.popleft()
       if first_char != last_char:
          result = "This is not a palindrome"
          break
       else:
           result = 'This is a palindrome'

    return result

print(is_palindrome('Red rUm, Sir, is murDer'))
print(is_palindrome('nO Lemon, No meloN'))
print(is_palindrome('nEver Odd or eVen'))
print(is_palindrome('Believe it or not'))
print(is_palindrome('Prime Minister of Cambodia'))