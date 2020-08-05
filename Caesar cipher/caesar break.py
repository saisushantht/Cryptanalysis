def decrypt(string, shift):
  plain = ''                                                     #intilizing string to store cipher text
  for char in string:                                             
    if char == ' ':                                                #to add space as it is
      plain = plain + char                                       
    elif  char.isupper():                                          #to apply the encryption on the upper case letters 
      plain = plain + chr((ord(char) - shift - 65) % 26 + 65)    #for upper case letters to shift eith ASCII values 
    else:                                                             
      plain = plain + chr((ord(char) - shift - 97) % 26 + 97)    #for lower case letters to shift eith ASCII values
  
  return plain

text = input()
a=1
common_words=["the","of","and","in","is","you","that","it","which"]
while a:
    a+=1
    co_text=decrypt(text,a)
    #print(co_text,a)
    for i in co_text.split(" "):
        if i in common_words:
            print(co_text)
            if(input("1-Yes , 0-No \nAre you satisfied:")):
                print("Key=",a)
                a=False
                break