#!/usr/bin/python3

#     Copyright (C) 2023 @servo
#     https://github.com/servomekanism/transgreek
# 
#     transgreek - Translate a greek-lettered wordlist to greeklish. May 
#     have some dups as some greek words that are written with different 
#     greek letters can produce the same greeklish output.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
#     For more see the file 'LICENSE' for copying permission.

import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python3 %s <input_file> <output_file>" % sys.argv[0])

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

input_file  = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f, open(output_file, 'w') as outfile:
    Lines = f.readlines()
    for line in Lines:
        perm_1 = line.translate(greek2latin_xuw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_2 = line.translate(greek2latin_xuo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_3 = line.translate(greek2latin_xyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_4 = line.translate(greek2latin_xyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_5 = line.translate(greek2latin_huw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_6 = line.translate(greek2latin_huo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_7 = line.translate(greek2latin_hyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_8 = line.translate(greek2latin_hyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace(" ", "")
        perm_9 = line.translate(greek2latin_xuw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_10 = line.translate(greek2latin_xuo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_11 = line.translate(greek2latin_xyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_12 = line.translate(greek2latin_xyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_13 = line.translate(greek2latin_huw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_14 = line.translate(greek2latin_huo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_15 = line.translate(greek2latin_hyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_16 = line.translate(greek2latin_hyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_17 = line.translate(greek2latin_xuw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_18 = line.translate(greek2latin_xuo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_19 = line.translate(greek2latin_xyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_20 = line.translate(greek2latin_xyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_21 = line.translate(greek2latin_huw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_22 = line.translate(greek2latin_huo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_23 = line.translate(greek2latin_hyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_24 = line.translate(greek2latin_hyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_25 = line.translate(greek2latin_xuw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_26 = line.translate(greek2latin_xuo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_27 = line.translate(greek2latin_xyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_28 = line.translate(greek2latin_xyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_29 = line.translate(greek2latin_huw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_30 = line.translate(greek2latin_huo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_31 = line.translate(greek2latin_hyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_32 = line.translate(greek2latin_hyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace("B", "V").replace("b", "v").replace(" ", "")
        perm_33 = line.translate(greek2latin_xuw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("X", "Ch").replace("x", "ch").replace(" ", "")
        perm_34 = line.translate(greek2latin_xuo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("X", "Ch").replace("x", "ch").replace(" ", "")
        perm_35 = line.translate(greek2latin_xyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("X", "Ch").replace("x", "ch").replace(" ", "")
        perm_36 = line.translate(greek2latin_xyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("X", "Ch").replace("x", "ch").replace(" ", "")
        perm_37 = line.translate(greek2latin_xuw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace("X", "Ch").replace("x", "ch").replace(" ", "")
        perm_38 = line.translate(greek2latin_xuo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace("X", "Ch").replace("x", "ch").replace(" ", "")
        perm_39 = line.translate(greek2latin_xyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace("X", "Ch").replace("x", "ch").replace(" ", "")
        perm_40 = line.translate(greek2latin_xyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "Ks").replace("ξ", "ks").replace("B", "V").replace("b", "v").replace("X", "Ch").replace("x", "ch").replace(" ", "")

        #https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python
        perms_list = []
        perms_list.append(perm_1)
        perms_list.append(perm_2)
        perms_list.append(perm_3)
        perms_list.append(perm_4)
        perms_list.append(perm_5)
        perms_list.append(perm_6)
        perms_list.append(perm_7)
        perms_list.append(perm_8)
        perms_list.append(perm_9)
        perms_list.append(perm_10)
        perms_list.append(perm_11)
        perms_list.append(perm_12)
        perms_list.append(perm_13)
        perms_list.append(perm_14)
        perms_list.append(perm_15)
        perms_list.append(perm_16)
        perms_list.append(perm_17)
        perms_list.append(perm_18)
        perms_list.append(perm_19)
        perms_list.append(perm_20)
        perms_list.append(perm_21)
        perms_list.append(perm_22)
        perms_list.append(perm_23)
        perms_list.append(perm_24)
        perms_list.append(perm_25)
        perms_list.append(perm_26)
        perms_list.append(perm_27)
        perms_list.append(perm_28)
        perms_list.append(perm_29)
        perms_list.append(perm_30)
        perms_list.append(perm_31)
        perms_list.append(perm_32)
        perms_list.append(perm_33)
        perms_list.append(perm_34)
        perms_list.append(perm_35)
        perms_list.append(perm_36)
        perms_list.append(perm_37)
        perms_list.append(perm_38)
        perms_list.append(perm_39)
        perms_list.append(perm_40)
        
        perms_set = set(perms_list)

        for item in perms_set:
            outfile.write(item)
f.close()
