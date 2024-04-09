import java.util.Scanner;
  public class PercentDiscount {
     public static void main(String[] args) {

	Scanner keyz = new Scanner(System.in);
	System.out.println("Enter Value");
	float userInput = keyz.nextFloat();
	
	
	float calculatedValue = userInput * 0.1f;

	System.out.printf("The discount is: %.3f",calculatedValue);



}



}