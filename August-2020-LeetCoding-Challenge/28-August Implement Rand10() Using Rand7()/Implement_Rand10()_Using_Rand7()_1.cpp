// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    int rand10() {
        int initial = rand7();
        while(initial==7) {
            initial = rand7();
        }
        
        int less_than_or_equal_five = rand7();
        while(less_than_or_equal_five > 5) {
            less_than_or_equal_five = rand7();
        }
        
        return less_than_or_equal_five + (initial%2)*5;
    }
};
