class Solution {
    public int[] sumEvenAfterQueries(int[] A, int[][] queries) {
        int val =0;
        int ind =0;
        int sum = 0;
        int [] op = new int[A.length];
        for (int i =0;i<A.length;i++ ) {
        	val = queries[i][0];
        	ind = queries[i][1];
        	A[i] = A[i] + val;
        	for (int j =0;j<A.length;j++ ) {
        		if(A[j]%2==0){
        			sum = sum + A[j];

        		}

        	}
        	op[i]= sum;
        	sum =0;

        }
        return op;
    }

    public int removeDuplicates(int[] nums) {
    	// https://leetcode.com/problems/remove-duplicates-from-sorted-array/
        int i =0;
        int j = 0;
        int currElem = nums[0];
        int base = 0;
        while(j<nums.length){
        	while(j<nums.length && nums[i]==nums[j] ){
        		j++;
        	}
        	if(j==nums.length){
        		nums[base] = currElem;
        		base = base + 1;
        	}
        	else{
	        	nums[base] = currElem;
	        	
	        	currElem = nums[j];

	        	i =j;
	        	base = base + 1;
	       	}
        }
        
       
        return base;
    }

    public void test(){

    }

    public static void main(String[] args) {
    	Solution s = new Solution();
    	// int [] inp = {0,0,1,1,1,2,2,3,3,4,4};
		// System.out.println(s.removeDuplicates(inp));
        s.test();
    }
}