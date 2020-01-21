class Solution:
	def numUniqueEmails(self, emails):
		emails_set = set()
		for email in emails:
			emails_set.add(self.modify_email(email))
		return len(emails_set)

	def modify_email(self, email):
		split = email.split("@")
		split[0] = split[0].replace(".", "")
		split[0] = split[0].split("+")[0]
		email = split[0]+"@"+split[1]
		return email

if __name__ == '__main__':
	s= Solution()
	ip = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
	print(s.numUniqueEmails(ip))