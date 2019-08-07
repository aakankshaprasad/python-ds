class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = [""]
        if len(strs) == 0:
            c = ""
        elif len(strs) == 1:
            c = strs[0]
        else:
            totalsize = len(strs)
            size = len(strs[0])
            flag = 1
            for i in range(size + 1):
                second = first[0]

                # print (i)
                if flag == 1:
                    first = [w[0:i] for w in strs]
                    # print (first)
                    c = first[0]
                    count = 0
                    for w in first:
                        if c == w:
                            count += 1
                        else:
                            count -= 1
                    if count == totalsize:
                        flag = 1
                    else:
                        flag = 0
                        c = second
        # print c
        return c















