1.
Equivalent writing for s[::-1] of the form s[i:j:-1].

print(s[-1:-(len(s)+1):-1])

2.
Read a word s. Check whether s is a palindrome or a semipalindrome (made up of two equal halves).
#s="abcba" => palindrome
#s="abcabc" => semipalindrome

s=input()
if s[::1]==s[::-1]:
    print("This is a palindrom number")
elif len(s)%2==0 and s[:len(s)//2]==s[len(s)//2:len(s)]:
    print("This is a semipalindrom number")
else:
    print("No")
    
3.    
Read a string and a natural number k. Delete from s the character at position k (positions numbered from 0) and display the new string obtained

s=input()
k=int(input())
if k==0:
    print(s[1:len(s)])
else:
    print(s[0:k]+s[k+1:len(s)])    
    
4.
Read a word s.Display the string obtained by deleting the first vowel.

s=input()
for i in range(len(s)):
    if s[i].lower() in "aeiou" and i==0:
        s=s.replace(s[i],"",1)
        print(s)
        break
    elif s[i].lower() in "aeiou" and i>0:
        s=s[:i]+s[i+1:len(s)]
        print(s)
        break
else:
    print("String has no vowels")
    
5.
Read an s-word of no more than 10 characters. Show on a line the words obtained successively from s
#cutting the first and last letter (displayed centred on the 10 characters):
# algorithm
# lgorit
# gori
# or

s=input()
k=0
while k<len(s)//2:
    s=s.replace(s[k]," ",1)
    s=s.replace(s[len(s)-1-k]," ",1)
    print(s)
    k+=1

6.
a)Read a word w, a natural number p, a natural number n and a string of n words, each given on a line. Display all words that are p-rhymes of the w 
(i.e. the last p characters in the word coincide with the last p characters of w) and are at least p+2 in length. For example, for w = "cere", p = 2 ,
n = 4 and the words "pere", "teste", "are" and "programare", the words "pere" and "programare" must be displayed ("are" rhymes with ith "mere", but is 
shorter than p+2)

w=input()
p=int(input())
n=int(input())
c=""
while n>0:
    x=input()
    if x[len(x)-p:len(x)]==w[len(w)-p:len(w)] and len(x)>=p+2:
        c=c+x+" "
    n-=1
print(c)

b)Same requirement, but for words in a sentence where the words are separated by spaces.For example, for w = "cere", p = 2 , n = 4 and the sentence 
"Ana are mere si pere si banane de mancare", you must display the following result: 2-rhymes of the word 'cere' is: are mere pere mancare

w=input()
p=int(input())
n=int(input())
m=input()
c=""
z=" "
while len(m)>0:
    if z in m:
        poz=m.index(z)
        x = m[:poz]
        m = m[poz + 1:len(m)]
    else:
        x=m[:len(m)]
        m=""
    if x[len(x)-p:len(x)]==w[len(w)-p:len(w)]:
        c=c+x+" "
print(f"{p}-rimes of the word '{w}' are: {c}")

7.
Read a string s. Check if there is a string t, different from s, such that it can be obtained by concatenating an arbitrary number of times (𝑘>1) the 
string t (i.e. check whether the string s is periodic). If there are several such strings t it will be determined the longest. Example: the string 
s = abbaabbaabbaabba is obtained by concatenating the string t= abbaabba twice.

s=input()
for lun_per in range(len(s)-1,-1,-1):
    if len(s)%lun_per==0:
        if s==s[:lun_per]*(len(s)//lun_per):
            print(s[:lun_per])
            break
else:
    print("Sir is not periodic")
    
8.
a)Read a coded text according to the rule: in front of each character is written a number representing number of consecutive occurrences of this character
in the text. Write a program that reads the encoded text and decodes it, knowing that the original text contained no numbers. For example the encoded text
"1v3a1c1a1n1t5a2 1m13a1r4e" will decode "vaaacantaaaaa maaaaaaaaaaaaareeee"

s=input()
c=""
for i in range(len(s)):
    if s[i].isdigit()==True: # .isdigit()==True check if character is digit
        x=int(s[i])
    else:
        while x>0:
            c=c+s[i]
            x-=1
print(c)

b)Write a program that reads a given text on a line and encodes it according to the rule in a).

s=input()
x=s[0]
k=0
c=""
for i in range(len(s)):
    if x == s[i]:
        k=k+1
    else:
        c = c + str(k) + x
        k=1
        x=s[i]
c = c + str(k) + x
print(c)

9.
A word is read. Delete all occurrences of the first letter from the word: After deleting the letter 'X' the string obtained is 'S' of length L using 
different formatting.

s=input()
x=s[0]
s=s.replace(x,"")
print(f "After deleting the letter '{x}' the string obtained is \"{s}\" of length {len(s)}")

10.
Check (using first the find method, then the index method) whether a string t appears as a substring in a string s, and if so, display all positions where t
begins in s (non-overlapping occurrences), otherwise display a corresponding message. For example, string t= "abc" appears as a substring in string
s= "abccabcabababcc" starting at positions 0, 4 and 9.

#index method
s=input()
t=input()
p=s.index(t)
try:
    while p>=0:
        print(p)
        p=s.index(t,p+len(t))
except:
    pass

#find method
s=input()
t=input()
p=s.find(t)
while p!=-1:
    print(p)
    p=s.find(t,p+len(t))
    
11.
The same spelling mistake has been made in a sentence, possibly several times. A sentence and two strings s and t are read from the keyboard - the correct
one and the misspelled one, each of the three input data being given on a line

a)Display the correct sentence. For example, for the sentence "Problemele cu șiruri de caracteger nu sunt ggerle!",
# s="re" and t="ger" will display "Problemele cu șiruri de caractere nu sunt grele!".

prop=input()
s=input()
t=input()
prop=prop.replace(t,s)
print(prop)

b)Modify the program so that it reads a natural number p and corrects a maximum of p such errors (that do not overlap), and if there are more than p display
the message: "text contains too many errors, only p have been corrected"

prop=input()
s=input()
t=input()
p=int(input())
cor=prop.replace(t,s)
prop=prop.replace(t,s,p)
if cor==prop:
    print(prop)
else:
    print(f "The text contains too many errors, only {p} have been corrected")

12.
a)Write a program that replaces all occurrences of an s-word in a sentence with a word t(!word, not subscript). The words are separated by one or more spaces.
prop=input()
s=input()
t=input()
ls=[]
ls=prop.split()
prop1=""
for c in ls:
    prop1=c.replace(s,t)
    print(prop1,end=" ")
    
b)Same requirement as in a), but for the case where the words in the sentence are separated between them by spaces and the usual punctuation marks

prop=input()
ls=[]
ls=prop.split()
k=0
for c in ls:
    if k%2==0:
        print(c,end=" ")
    else:
        print(c,end=",")
    k+=1

13.
The figure of Caesar
a)Se citește un text și un număr natural k. Să se afișeze textul cifrat cu cifrul lui Cezar, prin care fiecare literă (!doar literele) este înlocuită cu 
litera aflată peste k poziții la dreapta în alfabet în mod circular(valoarea k reprezintă cheia secretă comună pe care trebuie să o cunoască atât expeditorul,
cât și destinatarul mesajului criptat). De exemplu, pentru textul "O zi frumoasa!" și k=9 se va afișa “X ir oadvxjbj! "

text=input()
k=int(input())
text_nou=""
import string
alfabet=list(string.ascii_lowercase)
ALFABET=list(string.ascii_uppercase)
for i in range(len(text)):
    if text[i].islower():
        c=alfabet.index(text[i])
        text_nou=text_nou+alfabet[(c+k)%26]
    elif text[i].isupper():
        c=ALFABET.index(text[i])
        text_nou=text_nou+ALFABET[(c+k)%26]
    else:
        text_nou=text_nou+text[i]
print(text_nou)

b)Read a natural number k and encrypted text with Caesar's cipher with key k. Display the decrypted text.

text=input()
k=int(input())
text_nou=""
import string
alfabet=list(string.ascii_lowercase)
ALFABET=list(string.ascii_uppercase)
for i in range(len(text)):
    if text[i].islower():
        c=alfabet.index(text[i])
        text_nou=text_nou+alfabet[(c-k)%26]
    elif text[i].isupper():
        c=ALFABET.index(text[i])
        text_nou=text_nou+ALFABET[(c-k)%26]
    else:
        text_nou=text_nou+text[i]
print(text_nou)

14.
A text is read from the keyboard. You are asked to "translate" the given text into gibberish: after each vowel add the letter p and once again that vowel 
(after a, e, i, o, u add respectively pa, pe,pi, po, pu). Example: "Ana are mere." becomes "Apanapa aparepe meperepe." Given such a text in gibberish,
can the original text be obtained? If so, write a program that receives a text in the gibberish language builds in memory and displays the original text.

normal -> gibberish

text=input()
vocale="aeiouAEIOU"
text_nou=""
for i in range(len(text)):
    c=vocale.find(text[i])
    if c!=-1:
        text_nou=text_nou+text[i]+"p "+text[i].lower()
    else:
        text_nou=text_nou+text[i]
print(text_nou)

gibberish -> normal
text=input()
vocale="aeiouAEIOU"
i=0
text_nou=""
while i<len(text):
    c=vocale.find(text[i])
    text_nou=text_nou+text[i]
    if c!=-1:
        i=i+3
    else:
        i=i+1
print(text_nou)

15.
Ana's electronic diary contains, every day, a sentence with information about the expenses she made that day. Write a program that reads one such sentence 
from Ana's diary and then display the total amount she spent that day. For example, for the sentence "Today I bought 5 RON worth of bread, I spent 10 RON on
milk and 15 RON on cheese. I also bought some slippers for 50 RON!",the program must show a total of 80 RON. The sentence is considered correct, i.e. 
all the numbers that appear in it are natural numbers representing the amounts Ana spent that day! 

phrase=input()
ls=[]
ls=phrase.split()
sum=0
for cuv in ls:
    if cuv.isdigit():
        sum=sum+int(cuv)
print(sum, "RON")

16.
Write a program that reads a string of characters and decides if this is a correct full name of a person.A full name is considered correct if it satisfies
the following properties: 
-the person can have at most two first names, and if there are two then they are separated by a hyphen ('-').The same applies to the surname 
-the surname or forename contains only letters and at most one hyphen. 
-every surname or forename consists of at least 3 letters. 
-every surname or forename begins with a capital letter. 
Example of correct full names: Ionescu-Cherea Mihai-Adrian,Popescu Elena-Maria, Vlad Matei and incorrect names: Ionescu-Cherea Mihai, Vlad Matei Alexandru

name=input()
ls=[]
ls=name.split()
print(ls)
print(len(ls))
gresit=0
print()
for cuv in ls:
    if cuv[0].isupper() and cuv[0].isalpha() and len(cuv)>=3:
        if cuv.find("-")==-1 and len(ls)>2:
            wrong=1
    else:
        wrong=1
if gresit==1:
    print("This name is not correct")
else:
    print("This name is correct")

17.
Read a sentence with words separated by spaces (one or more). Create a list of words that begin with a vowel (using comprehension)

s=input()
vocale="aeiou"
ls=s.split()
ls1=[]
ls2=[ls1.append(i) for i in ls if i[0] in vocale]
print(ls1)

18.
Caesar's cipher (using comprehension)

a)Create in memory a list of the small letters of the alphabet using comprehension and a word with all the lowercase letters of the alphabet

import string
lista_m=[]
ls=[]
lista_m=[ls.extend(string.ascii_lowercase)]
litere_mici=string.ascii_lowercase
print(ls)
print(litere_mici)

b)Read a text containing only the lower case letters of the English alphabet and the usual punctuation and a natural number k. Create in memory and display
the ciphertext with Caesar's cipher, whereby each letter in a given text is replaced by the letter located over 𝑘 positions to the right in the alphabet in 
a circular fashion (the value 𝑘 represents the key The common secret key to be known by both the sender and the recipient of the encrypted message).

text=input()
k=int(input())
text_nou=""
import string
alfabet=list(string.ascii_lowercase)
for i in range(len(text)):
    if text[i].islower():
        c=alfabet.index(text[i])
        text_nou=text_nou+alfabet[(c+k)%26]
    else:
        text_nou=text_nou+text[i]
print(text_nou)

