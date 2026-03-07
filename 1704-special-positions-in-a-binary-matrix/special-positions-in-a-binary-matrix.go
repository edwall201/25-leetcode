func numSpecial(mat [][]int) int {
    m := len(mat)
    n := len(mat[0])
    rowCount := make([]int, m)
    colCount := make([]int, n)

    for i:= 0; i <m ; i ++{
        for j:= 0; j <n; j ++{
            if(mat[i][j] == 1){
                rowCount[i] += 1
                colCount[j] +=1
            }
        }
    }

    ans := 0
    for i:=0; i <m ; i ++{
        for j:= 0; j <n; j ++{
            if(mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1){
                ans ++
            }
        }
    }

    return ans
}