// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
int maxProfit(int* prices, int pricesSize){
        int max = 0;
        int min = INT_MAX;
        for(int i=0;i<pricesSize;i++){
            if(prices[i]<min){
                min = prices[i];
            }
            else if(prices[i]-min>max){
                max = prices[i]-min;
            }
            
        }
        return max;
}
