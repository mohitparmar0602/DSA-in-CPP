class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int product = nums[0], n = nums.size();
        for(int i = 1, maxx = product, minn = product; i < n; i++){
            if(nums[i] < 0){
                swap(maxx, minn);
            }
            maxx = max(nums[i], maxx * nums[i]);
            minn = min(nums[i], minn * nums[i]);
            product = max(product, maxx);
        }
        return product;
    }
};