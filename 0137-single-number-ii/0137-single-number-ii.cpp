class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int l=nums.size();
        map<int,int>a;
        for(int i:nums){
            a[i]++;
        }
        for(auto&i:a){
            if(i.second==1){
                return i.first;
            }
        }
        return -1;
    
    }
};