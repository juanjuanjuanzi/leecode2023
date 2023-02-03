class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        length=len(colors)
        #统计符合条件的A的个数
        ca=cb=0
        i=0
        #print(colors)
        while i<(length-2):
            child=colors[i:i+3]           
            if child=='AAA':
                ca=ca+1
                if i==length-3:
                    break
                else:
                    i=i+3
                while colors[i]=='A':
                    ca=ca+1
                    i=i+1
                    if i==length:
                        break
            elif child=='BBB':           
                cb=cb+1
                if i==length-3:
                    break
                else:
                    i=i+3
                while colors[i]=='B':
                    cb=cb+1
                    i=i+1
                    if i==length:
                        break
            else:
                i=i+1
                  
        if ca<=cb:
            return False
        else:
            return True
