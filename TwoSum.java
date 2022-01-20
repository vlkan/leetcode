class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        int newArr[] = new int[2];
        
        for (int i=0; i<len; i++){
            for (int k=0; k<len; k++){
                if(k==i){
                    continue;
                }
                if (nums[i]+nums[k]==target){
                    newArr[0]=i;
                    newArr[1]=k;
                    break;
                }
            }
        }
        return newArr;
    }
}