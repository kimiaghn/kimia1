# text = 'hello world'
# d = []
# for c in text :
#  d.append(c)
#  d.append(ord(c))
# print(d)
import string
# text_weird = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
#  bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq()
#   gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
# discovery_sent = [ ]
# yz = ['y', 'z', 'Y', 'Z' ]
# ab = ['a', 'b', 'A', 'B']
#
# for i in text_weird :
#     if 97 <= ord(i) and ord(i) <= 143 :
#
#         discovery_sent.append(chr(ord(i)+2))
#
#
# print(*discovery_sent)

lower = string.ascii_lowercase
lower_case = lower[2:] + lower[:2]

upper = string.ascii_uppercase
upper_case = upper[2:] + upper[:2]

inputs = upper + lower
outputs = upper_case + lower_case

mapping_result = str.maketrans(inputs, outputs)

text_weird = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
result = text_weird.translate(mapping_result)
print(result)