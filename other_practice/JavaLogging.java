import java.util.logging.*;
public class JavaLogging {

    private static Logger logger;


    public static void main(String[] args) {
        

        try{
             String [] matrix = {"0010010", "1010101","1111111", "0010000","0000000"};
             System.out.println("Tushar");

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
int biggestPlus(String[] matrix) {
        char[][] charMatrix = new char [matrix.length][matrix[0].length()];
        char [] tempChar;
        int tempSize = 0;
        int maxSize = 0;
        for (int i=0;i<matrix.length;i++){
            tempChar = matrix[i].toCharArray();
            for (int j =0;j<matrix[0].length();j++)
                charMatrix[i][j] =tempChar[j];
        }
        for (int i=0;i<charMatrix.length;i++){
            for (int j=0;i<charMatrix[0].length;i++){
                if (charMatrix[i][j] == '1'){
                    tempSize = plus_size(i, j, charMatrix);
                    if (tempSize>maxSize){
                        maxSize = tempSize;
                    }
                }

            }
        }
        return maxSize;

    }

    int plus_size(int i,int j, char[][] matrix){
        int size = 0;
        char left = '2';
        char right = '2';
        char top = '2';
        char bottom = '2';

        while(true){
            left = '2';
            right = '2';
            top = '2';
            bottom = '2';
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
            if (left =='1' && right =='1' && top =='1' && bottom =='1'){
                size++;
            }
            else{
                return size;
            }
        }
    }

}