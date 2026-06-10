# Runtime: 68 ms (5.03%) 
# Memory: 12.22 mb (99.47%)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1_fin = False 
        num2_fin = False 
        carry = False 
        final = ListNode(0) 
        head = final

        if l1.val == 0 and l1.next == None:
            return l2 
        elif l2.val == 0 and l2.next == None: 
            return l1

        while num1_fin == False or num2_fin == False: 
            

            if num2_fin == True:
                sum = l1.val
            elif num1_fin == True:
                sum = l2.val
            else:
                sum = l1.val + l2.val 

            if carry == True: 
                sum += 1 
                carry = False 

            if sum > 9:
                sum = sum - 10 
                carry = True

            final.val = sum 
            

            if l1.next != None: 
                print(l1.val)
                l1 = l1.next 
            else: 
                num1_fin = True 

            if l2.next != None: 
                print(l2.val)
                l2 = l2.next 
            else: 
                num2_fin = True 
            if num1_fin == False or num2_fin == False:
                final.next = ListNode(0)
                final = final.next 

        if carry == True: 
            final.next = ListNode(1)
            

        return head 
        





  