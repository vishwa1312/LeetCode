def numUniqueEmails(self, emails):
    seen = set()
    for email in emails:
        local, domain = email.split('@')
        if '+' in local:
            local = local[:local.index('+')]
        seen.add(local.replace('.','') + '@' + domain)
    return len(seen)
#numUniqueEmails(2, "test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com")