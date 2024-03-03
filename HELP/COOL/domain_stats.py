import whois

domain = input("Enter your Domain: ")
domain_info = whois.q2(domain)

for key, value in domain_info.items():
    print(key,':', value)

