class
int biggestPlus(String[] matrix) {
    char[][] charMatrix = [matrix.length][matrix[0].length()];
    char [] tempChar;
    for (int i;i<matrix.length;i++){
        tempChar = matrix[i].toCharArray();
        for (int j;j<matrix[0].length();j++)
        charMatrix[i][j] =tempChar[j];
    }
    
}

int plus_size(int i,int j, String[][] matrix){
    int size = 0;
    char left = "2";
    char right = "2";
    char top = "2";
    char bottom = "2";
        
    while(true){
        left = "2";
        right = "2";
        top = "2";
        bottom = "2";
        try{
            left = matrix[i][j-1];
        }
        catch(Exception e){
            
        }
        try{
            right = matrix[i][j+1];
        }
        catch(Exception e){
            
        }
        try{
            top = matrix[i-1][j];
        }
        catch(Exception e){
            
        }
        try{
            bottom = matrix[i+1][j];
            
        }
        catch(Exception e){
            
        }
        if (left.equalsIgnoreCase("1") &&
            right.equalsIgnoreCase("1") &&
            top.equalsIgnoreCase("1") &&
            bottom.equalsIgnoreCase("1")){
            size++;
        }
        else{
            return size;
        }
    }
}