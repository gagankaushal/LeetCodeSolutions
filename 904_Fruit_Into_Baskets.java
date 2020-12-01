class Solution {
    public int totalFruit(int[] tree) {
        // max
        // count
        // swap
        
        // sliding window
        // time : O(n)
        // space : O(1)
        
        int lastFruit = -1;
        int secondLastFruit = -1;
        int curMax = 0;
        int lastFruitCount = 0;
        int max = 0;
        
        for(Integer fruit : tree){
            
            // max - find max
            if (fruit == lastFruit || fruit == secondLastFruit){
                curMax += 1;
            } else{
                curMax = lastFruitCount + 1;
            }
            
            // count
            if (fruit == lastFruit){
                lastFruitCount += 1;
            }else{
                lastFruitCount = 1;
            }
            
            // swap
            if (fruit != lastFruit){
                secondLastFruit = lastFruit;
                lastFruit = fruit;
            }
            
            
            // find best max
            max = Math.max(curMax, max);
            
        }
        
        return max;
        
    }
}
