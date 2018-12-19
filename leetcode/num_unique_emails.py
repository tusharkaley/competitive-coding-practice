class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        try:
        	count = 0
        	email_dict = dict()
        	for email in emails:
        		email_split = email.split("@")
        		name = email_split[0].split('+')[0]
        		name = name.replace(".", "")
        		domain = email_split[1]
        		if name in email_dict:
        			if domain not in email_dict[name]:
        				email_dict[name].append(domain)
        				count = count + 1 
        		else:
        			email_dict[name] = [domain]
        			count = count + 1
        	return count

        except Exception as e:
        	raise e 

if __name__ == "__main__":
    s = Solution()
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(s.numUniqueEmails(emails))
