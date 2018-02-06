class Solution(object):
    def readout(self, num):
        """
        :type head: ListNode
        :rtype: bool
        """
        belowTen = ['', 'one', 'two', 'three', 'for', 'five','six', 'seven', 'eight', 'nine']
        belowTwenty = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        belowHundred = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

        def helper(num):
            if num < 10: return belowTen[num]
            if num < 20: return belowTwenty[num - 10]
            if num < 100: 
                d = belowHundred[num/10 -1]
                if num%10: 
                    return d + " " + helper(num%10)
                return d 
            if num < 1000: 
                return belowTen[num/100] + ' hundred ' + helper(num%100) 
            if num < 1000000:
                return helper(num/1000) + ' thousand ' + helper(num%1000)
            return helper(num/1000000) + ' million ' + helper(num%1000000)

        return helper(num)


print Solution().readout(114123456)