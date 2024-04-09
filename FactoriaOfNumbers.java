import java.util.Scanner;
  public class FactoriaOfNumbers {
   public static void main(String[] args) {

	Scanner keyz = new Scanner(System.in);
	System.out.println("Enter Number");
	int num = keyz.nextInt();
	
	int count = 0;
	int total = 1;	

	if(num < 0) {
	System.out.println("Invalid number");}
	
	else {
	while(num > count) {
	int num1 = (num - count);
	count++;
	total *= num1;
	
	}
	System.out.println("The Factoria is :" + total);
	}

}


}
	