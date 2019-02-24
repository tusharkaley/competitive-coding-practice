// import java.util.*;
// public class Hello_java{
// 	public static void main(String[] args) {

// 		int [] array1 = new int[5];
// 		int [] array2 = new int[5];
// 		for (int i =0;i<array1.length ;i++ ) {
// 			array1[i] = i;
// 			array2[i]=i;
// 		}
// 		boolean areEqual = Arrays.equals(array1, array2);
// 		if (areEqual) {
// 			System.out.println("Tushar");
// 		}
// 		//useful code snippets

// 		//loop over array
// 		// int [] array1 = new int[5];
// 		for (int i =0;i<array1.length ;i++ ) {
// 			array1[i] = i;

// 		}
// 		//Dictionary JAVA
// 		HashMap<String, String> dict = new HashMap<String, String>();
// 		dict.put("Tushar", "Kaley");

// 		System.out.println(dict); 


// 		System.out.println(dict.get("Tushar"));
// 		System.out.println(dict.remove("England"));
// 		System.out.println(dict.size());

// 		for (String i : dict.keySet()) {
//   			System.out.println("key: " + i + " value: " + dict.get(i));
// 		}



// 	}

// }
class Test{
static void display(){
System.out.println("Buggy Bread");
}
}

class Hello_java{
public static void main(String... args){
Test t = null;
t.display();
}
}
