set<string> combinations(string s, int l) {
    int mask = 1<<s.length();
    set<string> coll;
    string curr = "";
    for(int i=1;i<mask;i++) {
        int num = i;
        int j = 0;
        while(num) {
            if(num&1)
                curr = curr + s[j];
            j++;
            num>>= 1;
        }
        if(curr.length() == l)
            coll.insert(curr);
        curr = "";
    }
    return coll;
}


class CombinationIterator {
public:
    set<string> s1;
    set<string>::iterator itr;
    
    CombinationIterator(string characters, int combinationLength) {
        this->s1 = combinations(characters, combinationLength);
        this->itr = begin(s1);
    }
    
    string next() {
       return !(itr == end(s1)) ? *itr++ : "";
    }
    
    bool hasNext() {
        return !(itr == end(s1));      
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
