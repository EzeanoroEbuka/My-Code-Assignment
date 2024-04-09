import java.util.Scanner;
public class DataType {
public static void main(String[] args) {

	Scanner keyz = new Scanner(System.in);
	System.out.println("Enter Numerator");
	int input = keyz.nextInt();

	System.out.println("Enter Denominator");
	int input2 = keyz.nextInt();

	if(input % input2 != 0)
	System.out.println("A 'float' Data Type");

	else 
	System.out.println("An 'int' Data Type");

}



}