import java.util.Scanner; 
  public class Remainders {
    public static void main(String[] args) {

	Scanner keyz = new Scanner(System.in);
	System.out.println("Enter numerator");
	float input1 = keyz.nextFloat();	

	System.out.println("Enter denominator");
	float input2 = keyz.nextFloat();

	float calculateInputs = input1 % input2;
	
	System.out.printf("The Remainder is:%.3f",calculateInputs);



}



}