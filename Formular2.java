import java.util.Scanner;
  public class Formular2 {
  public static void main(String[] args) {

	Scanner keyz = new Scanner(System.in);
	System.out.println("Enter number");
	int input = keyz.nextInt();

	int calculation = ((100 * input)/30);
	double formular = Math.sqrt(calculation);

	System.out.printf("The answer is: %.0f",formular);
	
	
	}


}