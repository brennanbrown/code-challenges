class Solution:
    def defang_IP(self, address):
        if "." in address:
            address = address.replace(".", "[.]")
        return address