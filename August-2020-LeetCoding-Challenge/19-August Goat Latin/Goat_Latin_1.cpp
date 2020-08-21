class Solution {
public:
    string toGoatLatin(string S) {
        stringstream str(S);
        string output;
        string word;
        int i=1;
        while(str>>word) {
            if( word[0]=='a' || word[0]=='e' || word[0]=='i' || word[0]=='o' || word[0]=='u' || word[0]=='A' ||word[0]=='E' || word[0]=='I' || word[0]=='O' || word[0]=='U') 
            {
                word+= "ma";
            }
            else {
                char temp = word[0];
                word.erase(word.begin());
                word.push_back(temp);
                word+="ma";
            }
            for(int j=1;j<=i;j++) {
                word+="a";
            }
            i++;
            output += word;
            output += " ";
        }
        output.erase(output.end()-1);
        return output;
    }
};
