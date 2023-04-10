#!/usr/bin/python3

import sys

greek_alphabet = 'ΆΑαάΒβΓγΔδΈΕεέΖζΉΗηήΊΙιίΚκΛλΜμΝνΌΟοόΠπΡρΣσςΤτΎΥυύΦφΧχΏΩωώ'

latin_alphabet_xuw = 'AAaaBbGgDdEEeeZzIIiiIIiiKkLlMmNnOOooPpRrSssTtUUuuFfXxWWww'
latin_alphabet_xuo = 'AAaaBbGgDdEEeeZzIIiiIIiiKkLlMmNnOOooPpRrSssTtUUuuFfXxOOoo'
latin_alphabet_xyo = 'AAaaBbGgDdEEeeZzIIiiIIiiKkLlMmNnOOooPpRrSssTtYYyyFfXxOOoo'
latin_alphabet_xyw = 'AAaaBbGgDdEEeeZzIIiiIIiiKkLlMmNnOOooPpRrSssTtYYyyFfXxWWww'
latin_alphabet_huw = 'AAaaBbGgDdEEeeZzIIiiIIiiKkLlMmNnOOooPpRrSssTtUUuuFfHhWWww'
latin_alphabet_huo = 'AAaaBbGgDdEEeeZzIIiiIIiiKkLlMmNnOOooPpRrSssTtUUuuFfHhOOoo'
latin_alphabet_hyo = 'AAaaBbGgDdEEeeZzIIiiIIiiKkLlMmNnOOooPpRrSssTtYYyyFfHhOOoo'
latin_alphabet_hyw = 'AAaaBbGgDdEEeeZzIIiiIIiiKkLlMmNnOOooPpRrSssTtYYyyFfHhWWww'

greek2latin_xuw = str.maketrans(greek_alphabet, latin_alphabet_xuw)
greek2latin_xuo = str.maketrans(greek_alphabet, latin_alphabet_xuo)
greek2latin_xyw = str.maketrans(greek_alphabet, latin_alphabet_xyw)
greek2latin_xyo = str.maketrans(greek_alphabet, latin_alphabet_xyo)
greek2latin_huw = str.maketrans(greek_alphabet, latin_alphabet_huw)
greek2latin_huo = str.maketrans(greek_alphabet, latin_alphabet_huo)
greek2latin_hyw = str.maketrans(greek_alphabet, latin_alphabet_hyw)
greek2latin_hyo = str.maketrans(greek_alphabet, latin_alphabet_hyo)

#θξψ  
# .replace("Ξ", "X").replace("ξ", "x")

#print('αυτο ειναι ενα παραδειγμα γιώργος καραγιαννίδης. Πονηρή αλεπού. Χαρίζω. Πολύ χύμα. Έθαψα. Έψαξα.'.translate(greek2latin_xuw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks"))

input_file  = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f:
    Lines = f.readlines()
    for line in Lines:
        perm_one   = line.translate(greek2latin_xuw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_two   = line.translate(greek2latin_xuo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_three = line.translate(greek2latin_xyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_four  = line.translate(greek2latin_xyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_five  = line.translate(greek2latin_huw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_six   = line.translate(greek2latin_huo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_seven = line.translate(greek2latin_hyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_eight = line.translate(greek2latin_hyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        
        #https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python

        perms_list = []
        perms_list.append(perm_one)
        perms_list.append(perm_two)
        perms_list.append(perm_three)
        perms_list.append(perm_four)
        perms_list.append(perm_five)
        perms_list.append(perm_six)
        perms_list.append(perm_seven)
        perms_list.append(perm_eight)
        perms_set = set(perms_list)
        #perms_final = list(perms_set)

        print(perms_set)

#        with open(output_file, 'w') as of:
#            of.write('\n'.join(perms_list))
f.close()
