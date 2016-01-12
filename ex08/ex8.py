# -*- coding: utf-8 -*-
formatter = "%r %r %s %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "三", "four")   # 'one' 'two' 三 'four'
print formatter % ("True", False, False, True)    # 'True' False False True

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#'I had this thing.' 'That you could type up right.' But it didn't sing. 'So I said goodnight.'
