import java.util.Scanner;
  public class SumOfDigits {
   public static void main(String[] args) {

	Scanner keyz = new Scanner(System.in);
	
	do {
	System.out.println("Enter First Number");
	int num1 = keyz.nextInt();
	
	System.out.println("Enter Second Number");
	int num2 = keyz.nextInt();

	int addition = (num1 + num2);
		
	

	
	System.out.println("The Sum Of The Numbers is :" + "\n" + addition);
	System.out.println("press -1 to contineu or 0 to stop");
	int input = keyz.nextInt();

	if(input == 0){
	break;
	}

	}while(true); 
	
	
	

      


    }

}