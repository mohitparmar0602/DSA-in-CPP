class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.size();
        int i = s.size()-1;

        while(s[i] == ' '){
            i--;
        }
        int count = 0;

        while(i >= 0 && s[i]!= ' '){
            count++;
            i--;
        }
        return count;

    }
};