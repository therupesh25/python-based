alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabets:
      position = alphabets.index(char)
      new_position = position + shift_amount
      end_text += alphabets[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
should_continue=False
while not should_continue:
    text= input("Enter the message : ")
    shift=int(input("Enter the shlft number : "))
    direction = input("Enter \"encrypt\" for encryption and \"decrypt\" for decryption :").lower()
    shift%=26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    n=input('y for continue and n for stop :').lower()
    if n=='n':
        should_continue=True
        
        print("good bye")
     
