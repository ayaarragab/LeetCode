int countDigits(int x){
    int count = 0;
    if(x == 0)
        return 1;
    if(x < 0)
        return -1;
    
    while(x > 0)
    {
        ++count;
        x /= 10;
    }
    return count;
}
bool compare(int x, int y){
    return x == y;
}
bool isPalindrome(int x) {
    if(countDigits(x) == -1)
        return false;
    else if(countDigits(x) == 1)
        return true;
    char buffer[50];
    sprintf(buffer, "%d", x);
    if(buffer[0] == buffer[countDigits(x) - 1])
    {
        if(countDigits(x) > 2)
        {
            for(int i = 1, j = countDigits(x) - 2; i != j && i < countDigits(x) && j >= 0; i++, j--){
                if(buffer[i] == buffer[j])
                    continue;
                else
                    return false;
            }
            return true;
        }
        else
            return true;
    }
    return false;
}