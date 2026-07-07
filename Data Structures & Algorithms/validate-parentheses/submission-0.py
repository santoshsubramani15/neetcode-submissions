class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        x={')':'(','}':'{',']':'['}
        for i in s:
            if i in x:
                if st and st[-1]==x[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return True if not st else False