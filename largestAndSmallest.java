import java.util.Scanner;
  public class largestAndSmallest {
  public static void main(String[] args) {
	Scanner keyz = new Scanner(System.in);

	int largestNumber = 0;
	int smallestNumber = 0;
	int i = 1;
	for(;i >0;i++) {
	System.out.println("Enter number");
	int input = keyz.nextInt();			
		
	if(input - largestNumber >= 0) {
	 largestNumber = input;
	}
	else {
	if(largestNumber - input <= 0)
	largestNumber = input;
	
	else {
	if(input - smallestNumber <= 0)
	smallestNumber = input;
	
	else {
	if(largestNumber - smallestNumber > 0)
	if(smallestNumber == 0){
	smallestNumber = input;}
	      }
	
            }
	}
	System.out.println("press '*' to contineu or '#' to stop");
	char input2 = keyz.next().charAt(0);
	if(input2 == '#')
	break;
	else
	if(input2 == '*');	
	
	}
	System.out.printf("Result : %n%d Largest Number%n%d Smallest number",largestNumber,smallestNumber);

}


}