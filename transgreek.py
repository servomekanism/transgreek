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
of = open(sys.argv[2], 'w')

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

        perm_nine       = line.translate(greek2latin_xuw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_ten        = line.translate(greek2latin_xuo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_eleven     = line.translate(greek2latin_xyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_twelve     = line.translate(greek2latin_xyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_thirteen   = line.translate(greek2latin_huw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_fourteen   = line.translate(greek2latin_huo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_fifteen    = line.translate(greek2latin_hyw).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        perm_sixteen    = line.translate(greek2latin_hyo).replace("Ψ", "Ps").replace("ψ", "ps").replace("Θ", "Th").replace("θ", "th").replace("Ξ", "X").replace("ξ", "x").replace(" ", "")
        
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
        perms_list.append(perm_nine)
        perms_list.append(perm_ten)
        perms_list.append(perm_eleven)
        perms_list.append(perm_twelve)
        perms_list.append(perm_thirteen)
        perms_list.append(perm_fourteen)
        perms_list.append(perm_fifteen)
        perms_list.append(perm_sixteen)

        perms_set = set(perms_list)

        # why doesn't the `with open(of, 'w')` work?
        for item in perms_set:
            of.write(item)
f.close()
