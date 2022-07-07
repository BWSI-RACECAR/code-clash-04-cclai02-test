class Solution:
    def validateName(self,input):
        # type input:string
        # return: bool
            
        x = set()

        for f in input:
            if f in x:
                return False
            else:
                x.add(f)
        return True

def main():
    string1 = input()

    tc1 = Solution()
    ans = tc1.validateName(string1)
    print(ans)

if __name__ == "__main__":
    main()
