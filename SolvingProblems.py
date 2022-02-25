#Valid Anagram

s1 = 'danger'
s2 = 'gardek'

def valid_anagram(string1: str, string2: str):
    string1 = string1.lower()
    string2 = string2.lower()

    if len(string1) == len(string2):
        for i in range(len(string1)):
            for j in range(len(string2)):
                if string1[i] == string2[j]:
                    pass
                else:
                    break

        return print(True)
    else:
        return print(False)


valid_anagram(s1,s2)