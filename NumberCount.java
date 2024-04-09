import java.util.Scanner;
  public class NumberCount {
  public static void main(String[] args) {

	Scanner keyz = new Scanner(System.in);
	int positive = 0;
	int negative = 0;
	int zeros = 0;

	for(int i = 1;i > 0;i++) {
	System.out.println("Enter Number");
	int num = keyz.nextInt();

	if (num > 0) {
	positive++;
	}
	
	else 
	if (num < 0) {
	 negative++;
	}
	else {
	zeros++;
	}
	
	System.out.println("press '*' to contineu or '#' to stop");
	char input = keyz.next().charAt(0);
	if(input == '#')
	break;
	else
	if(input == '*');	
	
	}
	System.out.printf("your Various input counts: %n%d positive numbers%n%d negative numbers%n%d zero",positive,negative,zeros);

      }


}