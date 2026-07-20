public class Solution {
    public string LongestPalindrome(string s) {

        int start=0;
        int max_len=1;
        int n=s.Length;
        for(int i=0; i<n; i++){
            int low=i;
            int high=i;

            while (low>=0 && high<n && s[low]==s[high]){
                int curr_len=high-low+1;

                if (curr_len>max_len){
                    start=low;
                    max_len=curr_len;

                }
                low-=1;
                high+=1;
            }

            low=i;
            high=i+1;

            while (low>=0 && high<n && s[low]==s[high]){
                int curr_len=high-low+1;

                if (curr_len>max_len){
                    start=low;
                    max_len=curr_len;

                }
                low-=1;
                high+=1;
            }

        
        }
        return s.Substring(start, max_len);
    }
}