import java.util.Scanner;
  public class SumInteger {
   public static void main(String[] args) {
	Scanner keyz = new Scanner(System.in);
	
	System.out.println("Enter Integers between 0 and 1000");
	int input = keyz.nextInt();
	
	
	if(input >= 1000) {
	 System.out.println("Explicit Integer");
	}
	else {
	if(input < 0) {
	System.out.println("Explicit Integer");}
	else {	
	int num1 = (input % 10);
	int num2 = (input / 10);
	int num3 = (num2 % 10);
	int num4 = (num2 / 10);

	int formular = (num4 + num3 + num1);
	
	System.out.println(formular);
	}
     }

}

}







