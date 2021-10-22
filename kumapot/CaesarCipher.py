from art import logo
print(logo)
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(plain_text,shift_amount,direction_action):
    result = ""
    shift_amount = shift_amount % 26
    if direction_action == "encode":
      for i in plain_text:
        num = ord(i) + shift_amount
        if num > 126:
          add = (num - 126) + 97
        else:
          add = num
        result += chr(add)
      print(f"The encoded text is {result}")

    elif direction_action == "decode":  
      for i in plain_text:
        num = ord(i) - shift_amount
        if num < 97:
          add = 26 + num
        else:
          add = num 
        result += chr(add)   
      print(f"The decoded text is {result}")
    else:
      print("Wrong input.")  

  caesar(plain_text = text, shift_amount = shift , direction_action = direction)

  final = input("Type 'Yes if you want to do this again. Otherwise type 'No'")
  if final == "No":
    should_continue = False
    print("Goodbye")
    break
