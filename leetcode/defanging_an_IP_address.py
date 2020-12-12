"""
Runtime: 16 ms, faster than 71.48% of Python online submissions for Defanging an IP Address.
Memory Usage: 13.4 MB, less than 87.28% of Python online submissions for Defanging an IP Address.
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        rtype = ""
        for i in range(len(address)):            
            if (address[i] == "."):
                rtype += "[.]"
            else:
                rtype += address[i]
        return rtype

ip = "1.1.1.1" #output "1[.]1[.]1[.]1"
ip = "255.100.50.0" #outout "255[.]100[.]50[.]0"
rtype = Solution.defangIPaddr(None, ip)
print(rtype)

"""
Runtime: 20 ms, faster than 38.87% of Python online submissions for Defanging an IP Address.
Memory Usage: 13.4 MB, less than 64.22% of Python online submissions for Defanging an IP Address.
"""

class Solution1(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        rtype = address.replace(".","[.]")

        return rtype

ip = "1.1.1.1" #output "1[.]1[.]1[.]1"
ip = "255.100.50.0" #outout "255[.]100[.]50[.]0"
rtype = Solution1.defangIPaddr(None, ip)
print(rtype)