class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        if(s.size() == 0) return 0;
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int res = 0;
        int cookie = s.size() - 1;
        for(int i = g.size() - 1;i >= 0; i--){
            if(cookie >= 0 && s[cookie] >= g[i]){
                res++;
                cookie--;
            }
        }
        return res;
    }
};