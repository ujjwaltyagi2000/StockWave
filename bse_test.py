from bsedata.bse import BSE
b = BSE()
print(b)
# Output:
# Driver Class for Bombay Stock Exchange (BSE)

# to execute "updateScripCodes" on instantiation
b = BSE(update_codes = True)

q = b.getQuote('534976')
print(q)

tg = b.topGainers()
print(tg)
# Output:
# [{'LTP': '2,255.80',
#   'change': '76.75',
#   'pChange': '3.52',
#   'scripCode': '534976',
#   'securityID': 'VMART'},
#  {'LTP': '274.30',
#   'change': '9.25',
#   'pChange': '3.49',
#   'scripCode': '538835',
#   'securityID': 'INTELLECT'},
#  {'LTP': '273.65',
#   'change': '9.20',
#   'pChange': '3.48',
#   'scripCode': '500620',
#   'securityID': 'GESHIP*'},
#  {'LTP': '3,092.55',
#   'change': '103.50',
#   'pChange': '3.46',
#   'scripCode': '539658',
#   'securityID': 'TEAMLEASE'},
#  {'LTP': '164.75',
#   'change': '5.45',
#   'pChange': '3.42',
#   'scripCode': '532636',
#   'securityID': 'IIFL'}]