#!/usr/bin/env python
# coding: utf-8
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

 

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

 

Note:

    Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
    There will be at most 10000 calls to StockSpanner.next per test case.
    There will be at most 150000 calls to StockSpanner.next across all test cases.
    The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

We have follow below approach -

Lets prices are [100,80,60.70,60,75,85]
So first find span of 100 its 1 ==> [1]
Now find span of 80 and compare with previous i.e. 100 ; 100 > 80  - so span [1,1]
Now find span of 60 and compare with previous i.e. 80 ; 80 > 60 - so span [1,1,1]
Now find span of 70 and compare with previous i.e. 60 ; 60 < 70  -- and span of 60 is 1
So now decrement 'i' by 1 and compare 'ith' element which is 80 but 80 > 70 so span [1,1,1,2]

Now find span of 60 and compare with previous i.e. 70 ; 70 > 60 - sp span [1,1,1,2,1]
Now find span of 75 and compare with previous i.e. 60 ; 60 < 75 now decrement 'i' by span of 60 which is 1
so now compare with 70 and 70 < 75 ; now again decremen 'i' by span of 70 which is 2
now compare with 80 (instead of 60 as we decrement span of 2) so 80 > 75 so span  [1,1,1,2,1,4]

So in this way we skipped few members.
# In[ ]:


class StockSpanner(object):

    def __init__(self):
        global spans 
        spans = []
        global prices 
        prices = []
    
    def next(self, price):
        indx = len(prices) - 1
        while(indx >=0 and prices[indx] <= price):
            indx = indx - spans[indx]
        
        prices.append(price)
        span = len(prices) - 1 - indx
        spans.append(span)
        return span

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
price = int(input())
param_1 = obj.next(price)

