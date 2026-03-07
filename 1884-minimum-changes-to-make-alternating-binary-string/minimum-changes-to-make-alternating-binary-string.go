func minOperations(s string) int {
    countA := 0
    for i:= 0; i < len(s); i ++{
        var expected byte
        if i %2 == 0{
            expected ='0'
        }else{
            expected = '1'
        }
        if s[i] != expected{
            countA ++
        }
    }
    countB := len(s) - countA
    
    if countA < countB {
        return countA
    }
    return countB
    
}